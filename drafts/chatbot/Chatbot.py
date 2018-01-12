import os
from chatterbot import ChatBot

if os.path.exists('./db.sqlite3'):
    chatbot = ChatBot(
        'Ron Obvious',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
        database='./db.sqlite3'
    )
else:
    chatbot = ChatBot(
        'Ron Obvious',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )
    chatbot.train("chatterbot.corpus.romanian")

while 1:
    user_input = raw_input(">> ")
    print(chatbot.get_response(user_input))
