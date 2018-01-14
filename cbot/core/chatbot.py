import json
from difflib import SequenceMatcher
from random import choice

from cbot import utils


class ACTION:
    NOTHING = 0
    IS_ANSWERING = 1
    IS_QUESTIONING = 2
    EXIT = 3

class DATA:
    LINES = "lines.json"
    RESPONSES = "responses.json"

LINES, RESPONSES = map(lambda arg: json.loads(utils.get_res(arg)),
                       [DATA.LINES, DATA.RESPONSES])


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
    print(message)


def receive_message():
    return raw_input('> ')


def pick_random_line(topic):
    if topic not in LINES:
        print("Scrie topicul corect")
        return "Nu am inteles bine, te rog repeta"
    return choice(LINES[topic])


def main():
    current_action = ACTION.NOTHING
    send_message(pick_random_line('greeting'))

    while True:
        if current_action == ACTION.NOTHING:
            send_message(pick_random_line('initialize'))
            while True:
                message = receive_message()
                category = check_response(message)
                if category == 'no_category':
                    pick_random_line('try_again')
                elif category == 'initialize_questioning':
                    current_action = ACTION.IS_QUESTIONING
                    break
                elif category == 'initialize_answering':
                    current_action = ACTION.IS_ANSWERING
                    break

        if current_action == ACTION.IS_ANSWERING:
            'do_shit'

        if current_action == ACTION.IS_QUESTIONING:
            'do_shit'

        if current_action == ACTION.EXIT:
            'do_shit'

        break


class Chatbot(object):

    def __init__(self):
        self.current_action = ACTION.NOTHING
        self.question_happened = True

    def communicate(self, message):
        if self.current_action == ACTION.NOTHING:
            if not self.question_happened:
                self.question_happened = True
                return pick_random_line('initialize')
            category = check_response(message)
            if category == 'no_category':
                return pick_random_line('try_again')
            elif category == 'initialize_questioning':
                self.current_action = ACTION.IS_QUESTIONING
                self.question_happened = False
                return self.communicate(message)
            elif category == 'initialize_answering':
                self.current_action = ACTION.IS_ANSWERING
                self.question_happened = False
                return self.communicate(message)

        if self.current_action == ACTION.IS_ANSWERING:
            if not self.question_happened:
                self.question_happened = True
                return 'Ask away.'
            # Process question and get answer.
            answer = 'something'
            return 'Here is your answer'

        if self.current_action == ACTION.IS_QUESTIONING:
            if not self.question_happened:
                self.question_happened = True
                return 'Asking question'
            # Check if answer is correct.


if __name__ == '__main__':
    main()
