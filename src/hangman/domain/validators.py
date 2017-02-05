"""
validators Module

Created on 30.01.2017
@author adiM
"""


class HangmanException(Exception):
    pass


class SentenceValidatorException(HangmanException):
    pass


class SentenceValidator(object):
    @staticmethod
    def validate(sentence):
        if sentence == '':
            raise SentenceValidatorException("Introduce at least one word")
        words = sentence.split(' ')
        for w in words:
            if len(w) < 3:
                raise SentenceValidatorException("Words must have at least 3 letters.")
