import logging
import os
import sys

FORMAT_VERBOSE = '[stepauto.%(name)s] [%(process)d] [%(threadName)s] %(module)s %(funcName)s %(levelname)s: %(message)s'

_logger = None

def init_logger(name=None, filename='stepauto.log', format=FORMAT_VERBOSE,
                level=logging.DEBUG, echo=False):

    global _logger

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(filename=filename)
    handler.setFormatter(logging.Formatter(format))
    handler.setLevel(level)

    logger.addHandler(handler)

    if echo is True:
        echo_handler = logging.StreamHandler(sys.stdout)
        echo_handler.setFormatter(logging.Formatter(format))
        echo_handler.setLevel(logging.DEBUG)
        logger.addHandler(echo_handler)

    _logger = logger

    return _logger
