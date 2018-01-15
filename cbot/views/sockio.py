"""Websockets module used to handle all socket.io connections."""


from flask_socketio import emit

from cbot import sio
from cbot.core import chatbot


CHAT = "chat"
TIMEOUT = 1    # we should return a result under this timeout (seconds)

bot = chatbot.Chatbot()


# FIXME(cmiN): maybe we'll want to put this behind a namespace.
@sio.on(CHAT)
def chat_message(message):
    """Gives a reply for the received `message`.

    :returns: True if reply succeeded, False otherwise
    """
    response = bot.communicate(message)
    emit(CHAT, response)
    return True
