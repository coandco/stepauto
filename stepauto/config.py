from ConfigParser import RawConfigParser
import logging

from stepauto.conf import PATH
from stepauto.logger import init_logger

_config_parser, _logger = None, None

PATH = "stepauto.conf"

class ConfigNotInitialized(Exception):
    """Exception raised when config.init has not been called"""


def _init_logger(config_parser, service_name, echo=False):
    logging_values = dict(config_parser.items('logging'))

    override_section = 'logging.%s' % (service_name, )
    if config_parser.has_section(override_section):
        override_values = dict(config_parser.items(override_section))
        logging_values.update(override_values)

    # Decode 'level'
    if 'level' in logging_values:
        level = logging_values.get('level')
        if level:
            logging_values['level'] = getattr(logging, level)
        else:
            # An empty key
            del logging_values['level']

    return init_logger(name=service_name, echo=echo, **logging_values)


def init(service_name, config_file=PATH, logger=None, echo=False):
    global _config_parser, _logger

    config_parser = RawConfigParser()
    config_parser.read(config_file)

    _config_parser = config_parser
    if logger is None:
        logger = _init_logger(config_parser, service_name, echo=echo)
    _logger = logger


def get_logger():
    if _logger is None:
        raise ConfigNotInitialized
    return _logger


def get_config_parser():
    if _config_parser is None:
        raise ConfigNotInitialized
    return _config_parser
