"""
sentence_controller Module

Created on 30.01.2017
@author adiM
"""


class SentenceController(object):
    """
        The controller that manages the loading and saving of sentences from file and creating new sentences
    """
    def __init__(self, sentence_repository):
        """
            SentenceController constructor - initialize the controller the specific repository and loads the
            repository with data

            Parameters: sentence_repository - the repository containing the sentences
        """
        self.__sentence_repository = sentence_repository
        self.__sentence_repository.load_sentences()

    def add_sentence(self, sentence):
        """
            Adds a new sentence to the game

            Parameters: sentence - new sentence to be stored - string
        """
        self.__sentence_repository.save(sentence)

    def save_to_file(self):
        """
            Saves the current repository content to a file
        """
        self.__sentence_repository.save_sentences()

    def get_all(self):
        """
            Return a list with all the sentences
        """
        return self.__sentence_repository.get_all()