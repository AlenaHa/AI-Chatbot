import os
import unittest

from cbot import settings
from cbot.core import answer


class TestAnswer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ans = answer.Answer(settings.DEF_NAMES)

    def test_defs(self):
        tests = [
            ("psiho", "studiul proceselor psihologice in raport"),
            ("psihomotor", "referitor la miscari care implica activitatea"),
            ("portocala", None),
        ]
        for word, defin in tests:
            _defin = self.ans.get_answer(word)
            expr = _defin.startswith(defin) if _defin else _defin == defin
            self.assertTrue(expr)

    def test_figure_word(self):
        tests = [
            ("ce este inima?", "inima"),
            ("la ce ajuta ficatul meu ?", "ficatul meu"),
            ("Ce-i aia splina?", "splina"),
        ]
        for question, word in tests:
            self.assertEqual(word, self.ans.figure_word(question))


if __name__ == "__main__":
    unittest.main(failfast=True)
