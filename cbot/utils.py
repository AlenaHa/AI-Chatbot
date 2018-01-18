"""Various general purpose utilities."""


import base64
import hashlib
import logging
import os

import functools32

from cbot import settings


def read(fpath, content=True):
    abspath = os.path.join(settings.PROJECT, fpath)
    if not content:
        return abspath
    with open(abspath) as stream:
        return stream.read()


@functools32.lru_cache()
def get_secret_key():
    """Return a SHA256 hash as the default secret key."""
    # Obtain key bytes from default path.
    key_data = read(settings.SECRET_KEY_PATH)
    key = base64.b64decode(key_data)
    # Compute and return key hash.
    return hashlib.sha256(key).digest()


def get_res(name, content=True):
    """Return a resource path or content by giving a relative `name`.

    :arg str name: relative name of the resource
    :key bool content: return the content if `True`, otherwise the
    absolute path

    >>> utils.get_res("training-data/ai.yml", content=False)
    '/home/cmin/Repos/AI-Chatbot/res/cbot/training-data/ai.yml'
    >>> utils.get_res("training-data/ai.yml")
    'categorii:...'
    """
    path = os.path.join(settings.RES, name)
    return read(path, content=content)


def get_logger(name, use_logging=settings.LOGGING, debug=settings.DEBUG):
    """Obtain a logger object given a name."""
    log = logging.getLogger(name)
    if settings.LOGFILE:
        handler = logging.FileHandler(settings.LOGFILE)
    else:
        handler = logging.StreamHandler()
    template = "%(levelname)s - %(name)s - %(asctime)s - %(message)s"
    formatter = logging.Formatter(template)
    handler.setFormatter(formatter)
    if not log.handlers:
        log.addHandler(handler)
        level = logging.DEBUG if debug else logging.INFO
        level = level if use_logging else logging.CRITICAL
        log.setLevel(level)
    return log


class Logger(object):

    """Simple base class offering logging support."""

    def __init__(self, logging=settings.LOGGING, debug=settings.DEBUG):
        """Log information using the `log` method.

        :param bool logging: enable logging or not
        :param bool debug: enable debugging messages
        """
        super(Logger, self).__init__()
        self.log = get_logger(__file__, use_logging=logging, debug=debug)
