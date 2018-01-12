"""API exposing extracted profiles data."""


from flask_restful import request, abort

from cbot import schemas, settings, utils
from cbot.views.api import base
from cbot.core.Chatbot import Chatbot


URL_PREFIX = "/chat"


class ChatResource(base.BaseResource):
    def __init__(self):
        self.bot = Chatbot()
    ENDPOINT = "chat"

    def get(self):
        """Start chatting with the chatbot."""
        msg = request.args.get("message")
        if not msg:
            return {"message": "missing 'message' query parameter"}, 400
        response = self.bot.communicate(msg)
        return {"data": response}
