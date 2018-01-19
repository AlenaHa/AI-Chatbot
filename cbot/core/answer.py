"""Try to answer to user questions."""


import re
import xml.etree.ElementTree as ET

from cbot import utils


class Answer(object):

    STRIP = "* \n"
    NO_ANSWER = "Nu stiu raspunsul la intrebarea ta."

    RE_END = re.compile(
        r"(\w\.){2}|,-a adj.|, -oare adj.",
        re.IGNORECASE | re.MULTILINE
    )
    _QUES = [
        r"(ce este aia|ala)",
        r"ce este",
        r"la ce se refera",
        r"ce inseamna",
        r"ce-i (aia|ala)",
        r"la ce ajuta"
    ]
    RE_QUES = re.compile(
        r"({})\s+(?P<word>.+?)\s*\?".format(r"|".join(_QUES)),
        re.IGNORECASE | re.MULTILINE
    )

    def __init__(self, res_names):
        self._defs = {}
        self._load(res_names)

    @classmethod
    def _parse_defs(cls, root):
        norm = lambda arg: arg.text.strip(cls.STRIP).lower()
        for categ in root.findall("category"):
            pattern, template = map(norm, categ.getchildren())
            yield cls.RE_END.sub("", pattern).strip(), template

    def _load(self, res_names):
        for res_name in res_names:
            fpath = utils.get_res(res_name, content=False)
            tree = ET.parse(fpath)
            for word, defin in self._parse_defs(tree.getroot()):
                self._defs[word] = defin

    def get_answer(self, word):
        word = word.lower().strip(self.STRIP)
        defin = self._defs.get(word)
        if defin:
            return defin
        chunks = set(word.split())
        chunks.add(word)

        for pattern, defin in self._defs.items():
            for chunk in chunks:
                if chunk in pattern or pattern in chunk:
                    return defin
        return None    # couldn't find anything

    def figure_word(self, question):
        match = self.RE_QUES.search(question)
        if match:
            return match.group("word")
        return None
