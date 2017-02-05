"""
test_sentenceRepository Module

Created on 03.02.2017
@author adiM
"""
from unittest import TestCase

from hangman.domain.validators import SentenceValidator, SentenceValidatorException
from hangman.repositories.sentence_repository import SentenceRepository, SentenceRepositoryException


class TestSentenceRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__sentence_repository = SentenceRepository(SentenceValidator)

    def test_save(self):
        s = "anna has apples"
        self.__sentence_repository.save(s)
        self.assertEqual(len(self.__sentence_repository.get_all()), 1, "Should be 1")
        self.assertRaises(SentenceRepositoryException, self.__sentence_repository.save, s)
        s = ""
        self.assertRaises(SentenceValidatorException, self.__sentence_repository.save, s)
        s = "I have a pen"
        self.assertRaises(SentenceValidatorException, self.__sentence_repository.save, s)
