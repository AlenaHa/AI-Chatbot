"""Base API views and functions."""


import urlparse

from flask_restful import (
    url_for,
    Resource,
)

from cbot import utils


ERRORS = {
    "ValueError": {
        "message": "invalid value",
        "status": 400,
    },
    "TypeError": {
        "message": "invalid key",
        "status": 400,
    },
}

URL_PREFIX = "/api"


def query2relative(endpoint, page_query):
    """Extend the relativity of a query-only URL."""
    url = url_for(endpoint)
    split = list(urlparse.urlsplit(url))
    split[3] = page_query.lstrip("?")
    return urlparse.urlunsplit(split)


class BaseResource(Resource):

    """Base resource API handler."""

    # TODO(cmiN): add here auth required decorator
    method_decorators = []
