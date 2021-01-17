#!/usr/bin/anv python3
# -*- coding: utf-8 -*-

import datetime
import requests
import tornado.ioloop
import tornado.web

AUTHORITY = {'district': '3',
             'city': '4'}

URL = 'https://corona-os.de/api/cases/graph.json?authority='
MAPPING = {'aktuell bestätigte Fälle': 'confirmed',
           'Wieder Gesund': 'recovered',
           'Verstorben': 'dead'}

HOUR_IN_SECONDS = 60 * 60

cache = None

def cache_valid():
    if not cache:
        return False
    age = datetime.datetime.now() - cache.updated
    return age.total_seconds() < HOUR_IN_SECONDS


class CoronaOsnaData():
    def __init__(self, metrics):
        self.updated = datetime.datetime.now()
        self.metrics = metrics


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        if not cache_valid():
            metrics = '# HELP corona_osnabrueck_cases Number of cases in Osna\n'
            metrics += '# TYPE corona_osnabrueck_cases gauge\n'
            for authority, index in AUTHORITY.items():
                url = URL + index
                print(f'Requesting data from {url}')
                data = requests.get(url).json().get('datasets')
                for series in data:
                    label = MAPPING.get(series.get('label'))
                    number = series.get('data')[-1]
                    metrics += f'corona_osnabrueck_cases{{type="{label}", '
                    metrics += f'authority="{authority}"}} {number}\n'
            global cache
            cache = CoronaOsnaData(metrics)
        self.set_header('content-type', 'text/plain; version=0.0.4')
        self.write(cache.metrics)


if __name__ == "__main__":
    app = tornado.web.Application([(r"/metrics", MainHandler)])
    print('Listening on port 8888')
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
