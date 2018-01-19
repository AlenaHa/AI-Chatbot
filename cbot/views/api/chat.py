"""API exposing extracted profiles data."""


from flask_restful import request

from cbot import settings
from cbot.core.answer import Answer
from cbot.core.chatbot import Chatbot
from cbot.views.api import base

URL_PREFIX = "/chat"

ans = Answer(settings.DEF_NAMES)
bot = Chatbot()


class ChatResource(base.BaseResource):

    ENDPOINT = "chat"

    def get(self):
        """Start chatting with the chatbot."""
        msg = request.args.get("message")
        if not msg:
            return {"message": "missing 'message' query parameter"}, 400

        response = bot.communicate(msg)

        return {"data": response}
