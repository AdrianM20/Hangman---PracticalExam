"""
sentence_repository Module

Created on 30.01.2017
@author adiM
"""
from hangman.domain.validators import HangmanException


class SentenceRepositoryException(HangmanException):
    pass


class SentenceRepository(object):
    """
        Repository for sentences which the game uses
    """
    def __init__(self, validator_class):
        """
            SentenceRepository constructor: initialize the Sentence Repository with a list container
            for storing sentences

            Parameters: validator_class - class that validates the repository input
        """
        self.__validator_class = validator_class
        self._sentences = []

    def find_sentence(self, sentence):
        """
            Checks if a specific sentence is already registered in the repository

            Parameter: sentence - the sentence to be found
            Return: the searched sentence if it exists as string,
                    None if the sentence was not found
        """
        for ent in self.get_all():
            if ent == sentence:
                return ent
        return None

    def save(self, sentence):
        """
            Saves a new sentence in the repository after checking if it doesn't exist and if it meets the
            validator's condition

            Parameters: the sentence to be saved - string
            Returns: -
            Exceptions: raises SentenceRepositoryException if the given sentence is already in the repository
        """
        if self.find_sentence(sentence) is not None:
            raise SentenceRepositoryException("Duplicate error. This sentence already exists")
        self.__validator_class.validate(sentence)
        self._sentences.append(sentence)

    def get_all(self):
        """
            Returns all the sentences - list
        """
        return self._sentences
