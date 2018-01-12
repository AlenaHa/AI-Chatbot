"""API exposing extracted profiles data."""


from flask_restful import request, abort

from cbot import schemas, settings, utils
from cbot.views.api import base


URL_PREFIX = "/chat"


class ChatResource(base.BaseResource):

    ENDPOINT = "chat"

    def get(self):
        """Start chatting with the chatbot."""
        msg = request.args.get("message")
        if not msg:
            return {"message": "missing 'message' query parameter"}, 400
        # TODO(Elena): aici apelam functia care intoarce o replica la mesaj.
        response = msg[::-1]    # mesajul inversat (de test; a se sterge)
        return {"data": response}
