#!/usr/bin/anv python3
# -*- coding: utf-8 -*-

import requests
import tornado.ioloop
import tornado.web

AUTHORITY = {'district': '3',
             'city': '4'}

URL = 'https://corona-os.de/api/cases/graph.json?authority='
MAPPING = {'aktuell bestätigte Fälle': 'confirmed',
           'Wieder Gesund': 'recovered',
           'Verstorben': 'dead'}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('# HELP corona_osnabrueck_cases Number of cases in Osna\n')
        self.write('# TYPE corona_osnabrueck_cases gauge\n')
        for authority, index in AUTHORITY.items():
            data = requests.get(URL + index).json().get('datasets')
            for series in data:
                label = MAPPING.get(series.get('label'))
                number = series.get('data')[-1]
                self.write(f'corona_osnabrueck_cases{{type="{label}", '
                           f'authority="{authority}"}} {number}\n')


if __name__ == "__main__":
    app = tornado.web.Application([(r"/metrics", MainHandler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
