import json
import re
import sqlite3
from difflib import SequenceMatcher
from random import choice

from chatterbot import ChatBot
from suds.client import Client

from cbot import utils, settings
from cbot.core import answer


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


def normalize(to_normalize):
    to_normalize = re.sub('\([^)]*\)', '', to_normalize)
    to_normalize = re.sub('[^\w\- ]', '', to_normalize)
    to_normalize = re.sub(' +', ' ', to_normalize)
    to_normalize = to_normalize.strip()
    to_normalize = to_normalize.lower()
    return to_normalize


def get_similarity(str1, str2):
    str1 = normalize(str1)
    str2 = normalize(str2)
    return SequenceMatcher(None, str1, str2).ratio()


def check_conditions(tokens1, tokens2):
    if 'sbj.' not in tokens1 or 'sbj.' not in tokens2:
        return False
    if not len(set(tokens1['ROOT']).intersection(set(tokens2['ROOT']))) > 0:
        return False
    if not len(set(tokens1['sbj.']).intersection(set(tokens2['sbj.']))) > 0:
        return False
    attr1 = []
    for deprel in tokens1:
        if 'ROOT' != deprel and 'sbj.' != deprel:
            attr1.extend(tokens1[deprel])
    attr2 = []
    for deprel in tokens2:
        if 'ROOT' != deprel and 'sbj.' != deprel:
            attr2.extend(tokens2[deprel])
    if not len(set(attr1).intersection(set(attr2))) > min(len(attr1), len(attr2)) / 2 + 1:
        return False
    return True


def xml_to_json(text):
    d = {}
    for line in text.split('<W')[1:]:
        word = str(line.split('>')[1].split('<')[0])
        deprel = str(line.split('deprel="')[1].split('"')[0])
        if deprel not in d:
            d[deprel] = []
        if word not in d[deprel]:
            d[deprel].append(word)
    return d


def are_answers_similar(answer1, answer2):
    ans = normalize(answer1)
    usr = normalize(answer2)

    client = Client('http://nlptools.info.uaic.ro/WebFdgRo/FdgParserRoWS?wsdl')
    usr_tokens = client.service.parseText(usr)
    ans_tokens = client.service.parseText(ans)

    ans_json_tokens = xml_to_json(ans_tokens)
    usr_json_tokens = xml_to_json(usr_tokens)

    return check_conditions(ans_json_tokens, usr_json_tokens)


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


def pick_random_line(topic):
    if topic not in LINES:
        print("Scrie topicul corect")
        print(topic)
        return "Nu am inteles bine, te rog repeta"
    return choice(LINES[topic])


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)


def get_random_question(user):
    print utils.get_res("database.db", False)
    db_conn = create_connection(utils.get_res("database.db", False))
    questions = [{'id': x[0], 'question': str(x[1]), 'answer': str(x[2])}
                 for x in db_conn.cursor().execute('select * from questions')]
    # print questions
    # difficulties = [re.split('.;?!', x['answer']) for x in questions]
    # print difficulties
    db_conn.close()
    return choice(questions)


class Chatbot:
    def __init__(self):
        self.current_action = ACTION.NOTHING
        self.question_happened = True
        self.question = {}
        self.off_topic = 0
        self.current_user = 1
        self.answerer = answer.Answer(settings.DEF_NAMES)
        self.chatbot = ChatBot(
            'Sefu la Bani',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            database=utils.get_res('db.sqlite3', False),
            tie_breaking_method="random_response"
        )

    def communicate(self, message):
        if self.current_action == ACTION.NOTHING:
            category = check_response(message)
            if category == 'no_category':
                if self.off_topic < 10:
                    self.off_topic += 1
                    return str(self.chatbot.get_response(message))
                else:
                    return 'Ia treceti la treaba, n-o mai luati la ...\n' + pick_random_line('initialize')

            elif category == 'initialize_questioning':
                self.off_topic = 0
                self.current_action = ACTION.IS_QUESTIONING
                self.question_happened = False
                return self.communicate(message)

            elif category == 'initialize_answering':
                self.off_topic = 0
                self.current_action = ACTION.IS_ANSWERING
                self.question_happened = False
                return self.communicate(message)

        if self.current_action == ACTION.IS_ANSWERING:
            category = check_response(message)
            print message
            print category
            if category == 'change':
                self.current_action = ACTION.NOTHING
                self.question_happened = False
                return pick_random_line('change_topic')
            if not self.question_happened:
                self.question_happened = True
                return pick_random_line('ask_me')
            word = self.answerer.figure_word(message)
            if word:
                response = self.answerer.get_answer(word) or pick_random_line('no_answer')
            else:
                response = pick_random_line('try_again')
            self.question_happened = False
            return response + '\n' + self.communicate(message)

        if self.current_action == ACTION.IS_QUESTIONING:
            category = check_response(message)
            if category == 'change':
                self.current_action = ACTION.NOTHING
                self.question_happened = False
                return pick_random_line('change_topic')
            if not self.question_happened:
                self.question_happened = True
                self.question = get_random_question(self.current_user)
                return str(self.question['question'])

            """Check if answer is correct"""
            if are_answers_similar(self.question['answer'], message):
                response = pick_random_line('right_answer')
            else:
                response = pick_random_line('wrong_answer')
            self.question_happened = False
            return response + ' ' + pick_random_line('next_question') + '\n' + self.communicate(message)
