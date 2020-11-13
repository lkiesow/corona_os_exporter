#!/usr/bin/anv python3
# -*- coding: utf-8 -*-

import requests
import tornado.ioloop
import tornado.web

URL = 'https://corona-os.de/api/cases/graph.json?authority=all'
MAPPING = {'aktuell bestätigte Fälle': 'confirmed',
           'Wieder Gesund': 'recovered',
           'Verstorben': 'dead'}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        data = requests.get(URL).json().get('datasets')
        self.write('# HELP corona_osnabrueck_cases Number of cases in Osna\n')
        self.write('# TYPE corona_osnabrueck_cases gauge\n')
        for series in data:
            label = MAPPING.get(series.get('label'))
            number = series.get('data')[-1]
            self.write(f'corona_osnabrueck_cases{{type="{label}"}} {number}\n')


if __name__ == "__main__":
    app = tornado.web.Application([(r"/metrics", MainHandler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
