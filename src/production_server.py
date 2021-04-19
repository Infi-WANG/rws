#!/usr/bin/env python
"""Production server launch file.

In production, RWS runs on Apache with mod_wsgi, so we need to do our
initialization at the top level and expose the Flask application.
"""

import server_factory
from wsgiref.simple_server import make_server


if __name__ == '__main__':
    server = server_factory.production()
    app = server._app
    httpd = make_server('0.0.0.0',5001,app)
    print('Serving HTTP on port 5001...')
    httpd.serve_forever()