"""Websockets module used to handle all socket.io connections."""


from flask_socketio import emit

from cbot import settings, sio
from cbot.core import answer, chatbot


CHAT = "chat"
TIMEOUT = 1    # we should return a result under this timeout (seconds)

ans = answer.Answer(settings.DEF_NAMES)
bot = chatbot.Chatbot()


# FIXME(cmiN): maybe we'll want to put this behind a namespace.
@sio.on(CHAT)
def chat_message(message):
    """Gives a reply for the received `message`.

    :returns: True if reply succeeded, False otherwise
    """

    word = ans.figure_word(message)
    print(word)
    if word:
        response = ans.get_answer(word) or answer.Answer.NO_ANSWER
    else:
        response = bot.communicate(message)

    emit(CHAT, response)
    return True
