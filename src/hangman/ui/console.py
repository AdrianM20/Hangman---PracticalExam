"""
console Module

Created on 30.01.2017
@author adiM
"""
from hangman.domain.validators import HangmanException


class Console(object):
    def __init__(self, sentence_controller, game_controller):
        self.__sentence_controller = sentence_controller
        self.__game_controller = game_controller

    def run_app(self):
        options = {1: self.__add_sentences,
                   2: self.__play_game,
                   3: self.__print_available_sentences}

        while True:
            self.__print_menu()
            option = input("Enter option: ")
            if option == "x":
                break
            try:
                option = int(option)
                options[option]()
            except ValueError as ve:
                print("Invalid input: ", ve)
                print("Try again!")
            except KeyError as ke:
                print("Option not available. Try again!")
            except HangmanException as he:
                print("An error occurred: ", he)
                print("Try again!")

    def __print_menu(self):
        print()
        print("What would you like to do?")
        print("\t1 - Add sentences to game")
        print("\t2 - Play Hangman")
        print("\tx - Exit app")

    def __add_sentences(self):
        print("Enter a sentence: ")
        sentence = input()
        self.__sentence_controller.add_sentence(sentence)
        self.__sentence_controller.save_to_file()

    def __print_available_sentences(self):
        sentences = self.__sentence_controller.get_all()
        for s in sentences:
            print(s)

    def __print(self, sentence, tries):
        hang = ["h", "a", "n", "g", "m", "a", "n"]
        if tries >= 0:
            print(sentence + ' - "{0}"'.format(''.join(hang[:tries + 1])))
        else:
            print(sentence + ' - ""')

    def __play_game(self):
        tries = -1
        self.__game_controller.start_game()
        self.__print(self.__game_controller.print_sentence(), tries)
        while True:
            if tries >= 6:
                print("YOU LOST! Good luck next time!")
                break
            letter = input("Enter a letter: ")
            if letter.isalpha():
                if self.__game_controller.is_letter(letter):
                    if self.__game_controller.is_available(letter):
                        self.__game_controller.fill_letter(letter)
                        if self.__game_controller.game_end():
                            print(self.__game_controller.print_sentence() + "\tYOU WON!!!\nPlay again?")
                            break
                        self.__print(self.__game_controller.print_sentence(), tries)
                    else:
                        tries += 1
                        self.__print(self.__game_controller.print_sentence(), tries)
                else:
                    tries += 1
                    self.__print(self.__game_controller.print_sentence(), tries)
            else:
                print("Incorrect input. Not a letter.")
