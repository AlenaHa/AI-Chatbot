import json
from random import choice
import sqlalchemy
from difflib import SequenceMatcher

ACTION_NOTHING = 0
ACTION_IS_ANSWERING = 1
ACTION_IS_QUESTIONING = 2
ACTION_EXIT = 3

LINES = {}
RESPONSES = {}
with open('cbot/resources/lines.json', 'r') as infile:
    LINES = json.load(infile)
with open('cbot/resources/responses.json', 'r') as infile:
    RESPONSES = json.load(infile)


def get_similarity(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()


def check_response(message):
    result = {}
    for response in RESPONSES:
        closest = sorted(RESPONSES[response],
                         key=lambda x: get_similarity(message, x),
                         reverse=True)[0]
        result[response] = closest
    final_result = sorted([response for response in result],
                          key=lambda x: get_similarity(message, result[x]),
                          reverse=True)[0]
    if get_similarity(result[final_result], message) >= .75:
        return final_result
    return 'no_category'


def send_message(message):
    print message


def receive_message():
    return raw_input('> ')


def pick_random_line(topic):
    if topic not in LINES:
        print "Nu mai fi bou si scrie topicu corect"
        return "Nu am inteles bine, te rog repeta"
    return choice(LINES[topic])


def connect(user='postgres', password='admin', db='AI-database', host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    connection = sqlalchemy.create_engine(url, client_encoding='utf8')
    metadata = sqlalchemy.MetaData(bind=connection, reflect=True)
    return connection, metadata


def main():
    current_action = ACTION_NOTHING
    send_message(pick_random_line('greeting'))

    while 1:
        if current_action == ACTION_NOTHING:
            send_message(pick_random_line('initialize'))
            while 1:
                message = receive_message()
                category = check_response(message)
                if category == 'no_category':
                    pick_random_line('try_again')
                elif category == 'initialize_questioning':
                    current_action = ACTION_IS_QUESTIONING
                    break
                elif category == 'initialize_answering':
                    current_action = ACTION_IS_ANSWERING
                    break

        if current_action == ACTION_IS_ANSWERING:
            'do_shit'

        if current_action == ACTION_IS_QUESTIONING:
            'do_shit'

        if current_action == ACTION_EXIT:
            'do_shit'

        break


class Chatbot():
    def __init__(self):
        self.current_action = ACTION_NOTHING
        self.question_happened = True

    def communicate(self, message):
        if self.current_action == ACTION_NOTHING:
            if not self.question_happened:
                self.question_happened = True
                return pick_random_line('initialize')
            category = check_response(message)
            if category == 'no_category':
                return pick_random_line('try_again')
            elif category == 'initialize_questioning':
                self.current_action = ACTION_IS_QUESTIONING
                self.question_happened = False
                return self.communicate(message)
            elif category == 'initialize_answering':
                self.current_action = ACTION_IS_ANSWERING
                self.question_happened = False
                return self.communicate(message)

        if self.current_action == ACTION_IS_ANSWERING:
            if not self.question_happened:
                self.question_happened = True
                return 'Ask away.'
            """Process question and get answer"""
            answer = 'something'
            return 'Here is your answer'

        if self.current_action == ACTION_IS_QUESTIONING:
            if not self.question_happened:
                self.question_happened = True
                return 'Asking question'
            """Check if answer is correct"""

#
# if __name__ == '__main__':
#     main()
