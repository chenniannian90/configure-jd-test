#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from tornado.web import RequestHandler
from raven.contrib.tornado import SentryMixin


logger = logging.getLogger('')


class BaseHandler(SentryMixin, RequestHandler):
    pass


class HelloHandler(BaseHandler):

    def get(self):
        logger.debug("debug", exc_info=True)
        logger.info("info", exc_info=True)
        logger.error("error", exc_info=True)
        logger.fatal("fatal", exc_info=True)
        self.write('Hello world!')


class ExcecptionHandler(BaseHandler):

    def get(self):
       raise Exception('ExcecptionHandler')
