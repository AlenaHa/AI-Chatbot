#! /usr/bin/env python

"""Tests general aspects of chatbot."""


import multiprocessing
import unittest

from socketIO_client import SocketIO

import cbot
from cbot.views import sockio


HOST = cbot.HOST if cbot.HOST != "0.0.0.0" else "localhost"
PORT = cbot.PORT

CHAT_EVENT = sockio.CHAT
CHAT_TIMEOUT = sockio.TIMEOUT


class BaseTest(unittest.TestCase):

    SERVER_PROC = None

    @classmethod
    def setUpClass(cls):
        cls.SERVER_PROC = multiprocessing.Process(
            target=cbot.run_server,
            kwargs={"conf": "testing"}
        )
        cls.SERVER_PROC.start()

    @classmethod
    def tearDownClass(cls):
        cls.SERVER_PROC.terminate()


class TestChatbot(BaseTest):

    def _chat_callback(self, status):
        self._status = status

    def _chat_event(self, message):
        self._message = message

    def setUp(self):
        self._status = None
        self._message = None

        self.sio = SocketIO(HOST, PORT)
        self.sio.on(CHAT_EVENT, self._chat_event)

    def tearDown(self):
        self.sio.disconnect()

    def _test_chat(self, msg, response=None):
        # Send message with callback.
        self.sio.emit(CHAT_EVENT, msg, callback=self._chat_callback)
        # Wait for the callbacks/events triggering.
        self.sio.wait(CHAT_TIMEOUT)
        # Now check the callback and received response.
        self.assertEqual(True, self._status)
        self.assertEqual(unicode, type(self._message))
        self.assertGreater(len(self._message), 0)
        if response:
            print(self._message)
            self.assertTrue(self._message.startswith(response))

    def test_chat_hello(self):
        self._test_chat("Salut!")

    def test_chat_questions(self):
        tests = [
            ("ce este aia inima?", "organ muscular cavitar situat in")
        ]
        for question, answer in tests:
            self._test_chat(question, response=answer)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    unittest.main(failfast=True)
