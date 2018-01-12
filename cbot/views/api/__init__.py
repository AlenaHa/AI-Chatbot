"""All views and routes exposed by the cbot web API."""


from . import (
    profiles,
    chat,
)
from .base import ERRORS, URL_PREFIX
from ... import api


JSON_REPR = "application/json"

output_default = api.representations[JSON_REPR]


@api.representation(JSON_REPR)
def output_json(data, code, *args, **kwargs):
    defaults = {
        "message": "ok",
        "status": code,
    }
    for default in defaults.items():
        data.setdefault(*default)
    return output_default(data, code, *args, **kwargs)


# Create endpoints to all exposed resources.

# For profiles.
api.add_resource(
    profiles.ProfilesResource,
    profiles.URL_PREFIX,
    endpoint=profiles.ProfilesResource.ENDPOINT
)
api.add_resource(
    profiles.ProfileResource,
    "{}/<profile_usafe>".format(profiles.URL_PREFIX),
    endpoint=profiles.ProfileResource.ENDPOINT
)

# For chat.
api.add_resource(
    chat.ChatResource,
    chat.URL_PREFIX,
    endpoint=chat.ChatResource.ENDPOINT
)
