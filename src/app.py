# -*- coding: utf-8 -*-

import logging.config

import tornado.web
import tornado.wsgi
import tornado.ioloop
from raven.contrib.tornado import AsyncSentryClient
from handler.hello_handler import HelloHandler, ExcecptionHandler
from settings import LOGGING_CONFIG, SENTRY_DSN
logging.config.dictConfig(LOGGING_CONFIG)


handlers = [
    (r'/', HelloHandler),
    (r'/except', ExcecptionHandler),
]


def get_tornado_application():
    application = tornado.web.Application(handlers)
    application.sentry_client = AsyncSentryClient(
        SENTRY_DSN,
        ignored_exception_types=[tornado.web.HTTPError]
    )
    return application


def get_wsgi_application():
    app = get_tornado_application()
    return tornado.wsgi.WSGIAdapter(app)


app = get_tornado_application()
wsgi_app = get_wsgi_application()


def run():
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run()