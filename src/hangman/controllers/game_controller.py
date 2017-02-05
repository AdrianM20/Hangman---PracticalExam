"""
game_controller Module

Created on 30.01.2017
@author adiM
"""

import random


class GameController(object):
    """
        The controller that manages the Hangman game
    """

    def __init__(self, sentence_repository):
        """
            GameController constructor - initialize the controller with the repository containing the sentences
            and prepares the sentence to be playes

            Parameters: sentence_repository - the repository containing the sentences
        """
        self.__sentence_repository = sentence_repository
        self.__game_sentence = ''
        self.__hidden_sentence = ''

    def __load_random_sentence(self):
        """
            Loads a random sentence from the repository

            Return: the randomly chosen sentence
        """
        l = len(self.__sentence_repository.get_all())
        r = random.randint(0, l - 1)
        return self.__sentence_repository.get_all()[r]

    def start_game(self):
        """
            Initializes a new sentence to pe played and creates the hidden version of it
        """
        self.__game_sentence = self.__load_random_sentence()
        self.__hidden_sentence = self.__create_sentence(self.__game_sentence)
        self.__hidden_sentence = self.__add_letters(self.__hidden_sentence)

    def fill_letter(self, letter):
        self.__hidden_sentence = self.__show_letter(self.__hidden_sentence, letter)

    def __create_sentence(self, game_sentence):
        """
            Creates a sentence with hidden letters from the original sentence

            Parameters: game_sentence - string
            Return: the sentence with hidden letters
        """
        words = game_sentence.split(' ')
        for e in range(0, len(words)):
            words[e] = self.__hide_letters(words[e])
        return '  '.join(words)

    def __add_letters(self, hidden_sentence):
        """
            Adds to the hidden_sentence the first and last letters of each word

            Parameters: hidden_sentence - string
            Returns: the sentence with it's necessary letters in place
        """
        for l in hidden_sentence:
            if l.isalpha():
                hidden_sentence = self.__show_letter(hidden_sentence, l)
        return hidden_sentence

    def __hide_letters(self, word):
        """
            Hides the letters of a word except the first and the last one

            Parameters: word - string
            Returns: the word with hidden letters
        """
        letters = [l for l in word]
        for l in range(1, len(letters) - 1):
            letters[l] = "_"
        return ' '.join(letters)

    def is_available(self, letter):
        for l in self.__hidden_sentence:
            if l == letter:
                return False
        return True

    def is_letter(self, letter):
        """
            Checks if a letter given by the user is contained by the hidden sentence

            Parameters: letter - to be checked
            Returns: True - if the letter is correct
                    False - if the letter is incorrect
        """
        for l in self.__game_sentence:
            if l == letter:
                return True
        return False

    def __show_letter(self, hidden_sentence, letter):
        """
            Checks if a given letter is contained by the hidden sentence and shows it if it's the case

            Parameters: hidden_sentence - the sentence to work with - strig
                        letter - the letter to be put in place
            Return: the new sentence with the letter revealed if it's the case
        """
        hidden_sentence = hidden_sentence.split(' ')
        for i, l in enumerate(self.__game_sentence):
            if l == letter:
                hidden_sentence[i] = letter
        return ' '.join(hidden_sentence)

    def print_sentence(self):
        """
            Return the sentence that is currently in game
        """
        return self.__hidden_sentence

    def game_end(self):
        h = self.__hidden_sentence.split(' ')
        h = ''.join(h)
        g = self.__game_sentence.split(' ')
        g = ''.join(g)
        return h == g
