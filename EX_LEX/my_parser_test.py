import unittest
from lex_code import lexicon
from my_parser import *

class TestSentence(unittest.TestCase):
    """Testing for class Sentence"""

    def setUp(self):
        self.subject=Sentence
        self.obj=Sentence
        self.verb=Sentence

    def test_parse_sentence(self):
        x=parse_sentence(lexicon.scan("go to the north and run"))
        self.assertEqual(x.subject,"player")
        self.assertEqual(x.object,"north")
        self.assertEqual(x.verb,"go")

unittest.main()



