"""API exposing extracted profiles data."""


from cbot.views.api import base


URL_PREFIX = "/profiles"


class ProfilesResource(base.BaseResource):

    ENDPOINT = "profiles"

    def get(self):
        """Returns a list of people in a paginated way."""
        return {"urls": ["not implemented yet"]}


class ProfileResource(base.BaseResource):

    ENDPOINT = "profile"

    def get(self, profile_usafe):
        """Returns data about a specific profile."""
        return {"data": "not implemented yet"}
