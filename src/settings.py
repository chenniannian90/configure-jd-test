# -*- coding: utf-8 -*-

SENTRY_DSN = "http://42d798d136f542f2af22fed1be6b56d9@localhost:9000/4"

# LOGGING 配置
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "loggers": {
        '': {
            'handlers': ['console', 'sentry'],
            'level': 'INFO',
            'propagate': False,
        },
        'tornado.access': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
        'tornado.application': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
        'tornado.general': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        }
    },
    "handlers": {
        'console': {
            'level': 'INFO',
            'formatter': 'console',
            'class': 'logging.StreamHandler',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': SENTRY_DSN,
        }
    },
    "formatters": {
        'console': {
                'format': '%(levelname)s %(asctime)s %(pathname)s %(lineno)d %(funcName)s "%(message)s'
            }
    }
}
