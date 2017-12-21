"""Various general purpose utilities."""


import base64
import hashlib
import logging
import os

import functools32

from cbot import settings


def read(fpath):
    with open(os.path.join(settings.PROJECT, fpath)) as stream:
        return stream.read()


@functools32.lru_cache()
def get_secret_key():
    """Return a SHA256 hash as the default secret key."""
    # Obtain key bytes from default path.
    key_data = read(settings.SECRET_KEY_PATH)
    key = base64.b64decode(key_data)
    # Compute and return key hash.
    return hashlib.sha256(key).digest()


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
