import sys
import re 
from lex import lex_list

class LEXICON():
    def scan(self,phrase):
    
        words=phrase.split()
        result=[]
        for word in words:
            if word in lex_list[0]:
                result.append(('direction',word))
            elif word in lex_list[1]:
                result.append(('noun',word))
            elif word in lex_list[2]:
                result.append(('stop',word))
            elif word in lex_list[3]:
                result.append(('verb',word))
            else:
                try:
                    result.append(('number',int(word)))
                except ValueError:
                    result.append(('error',word))
        print(result)
        return result
lexicon=LEXICON()
#sentence=input(">")
#lexicon.scan(sentence)