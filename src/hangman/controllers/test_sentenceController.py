"""
test_sentenceController Module

Created on 03.02.2017
@author adiM
"""
from unittest import TestCase

from hangman.controllers.sentence_controller import SentenceController
from hangman.domain.validators import SentenceValidator
from hangman.repositories.file_repository import SentenceFileRepository
from hangman.repositories.sentence_repository import SentenceRepository


class TestSentenceController(TestCase):
    def setUp(self):
        super().setUp()
        self.__sentence_repository = SentenceFileRepository(SentenceValidator, "../../../data/sentences.txt")
        self.__sentence_controller = SentenceController(self.__sentence_repository)

    def test_add_sentence(self):
        s = "anna has apples"
        self.__sentence_controller.add_sentence(s)
        self.assertEqual(len(self.__sentence_controller.get_all()), 1, "Should be 1")

    def test_save_to_file(self):
        s = "anna has apples"
        self.__sentence_controller.add_sentence(s)
        self.__sentence_controller.save_to_file()
