import re
import unittest
from lex_code import lexicon

class TestLexicon(unittest.TestCase):
    """tests for class lexicon"""

    def SetUp(self):
        lexicon

    def test_directions(self):
        self.assertEqual(lexicon.scan("north"),[('direction','north')])
        result = lexicon.scan('north south east')
        self.assertEqual(result,[('direction','north'),
                                  ('direction','south'),
                                  ('direction','east')])

    
    def test_verbs(self):
        self.assertEqual(lexicon.scan('go'),[('verb','go')])
        result=lexicon.scan('go kill eat')
        self.assertEqual(result,[('verb','go'),
                                  ('verb','kill'),
                                  ('verb','eat')])

    def test_stops(self):
        self.assertEqual(lexicon.scan('the'),[('stop','the')])
        result=lexicon.scan("the in of")
        self.assertEqual(result,[('stop','the'),
                                  ('stop','in'),
                                  ('stop','of')])

    def test_nouns(self):
        self.assertEqual(lexicon.scan('bear'),[('noun','bear')])
        result=lexicon.scan('bear princess')
        self.assertEqual(result,[('noun','bear'),
                                 ('noun','princess')])
  
    def test_numbers(self):
        self.assertEqual(lexicon.scan('1234'),[('number',1234)])
        result=lexicon.scan('3 91234')
        self.assertEqual(result,[('number',3),
                                  ('number',91234)])

    def test_errors(self):
        self.assertEqual(lexicon.scan('ASDFAD'),[('error','ASDFAD')])
        result=lexicon.scan('bear IAS princess')
        self.assertEqual(result,[('noun','bear'),
                                  ('error','IAS'),
                                  ('noun','princess')])


unittest.main()                    