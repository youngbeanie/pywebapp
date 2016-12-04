#!/usr/bin/env python

import json
import web

urls = ('/', 'Default',
        '/api/(.*)', 'Api')

class Default:
    def GET(self):
        web.header('Content-Type', 'text/html')
        return """<html>
        <title>PyWebApp</title>
        <body>
        <h1>Hello World!</h1>
        <p>Available APIs</p>
        <ul>
        <li><a href="/api/v1/test">/api/v1/test</a></li>
        <li><a href="/api/v1/json">/api/v1/json</a></li>
        </ul>
        </body>
        </html>"""

class Api:
    def GET(self, name):
        if name == 'v1/test':
            return self.test()
        elif name == 'v1/json':
            return self.json()
        else:
            web.header('Content-Type', 'text/html')
            web.ctx.status = '404 Not Found'
            return "undefined"
    def test(self):
        web.header('Content-Type', 'text/html')
        return "test"
    def json(self):
        web.header('Content-Type', 'application/json')
        return json.dumps({'api-version': 'v1', 'app-name': 'pywebapp'})

web.config.debug = False
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()

# vim:ai ts=4 sw=4 et:
