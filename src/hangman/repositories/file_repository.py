"""
file_repository Module

Created on 30.01.2017
@author adiM
"""
from hangman.domain.validators import HangmanException
from hangman.repositories.sentence_repository import SentenceRepository


class SentenceFileRepositoryException(HangmanException):
    pass


class SentenceFileRepository(SentenceRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename

    def load_sentences(self):
        try:
            with open(self.__filename) as f:
                for line in f:
                    sentence = line.strip()
                    self.save(sentence)
            f.close()
        except IOError:
            raise SentenceFileRepositoryException("Error when reading from file")

    def save_sentences(self):
        try:
            with open(self.__filename, "w") as f:
                for s in self._sentences:
                    f.write(s + "\n")
            f.close()
        except IOError:
            raise SentenceFileRepositoryException("Error when writing to file")
