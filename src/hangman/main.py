"""
main Module

Created on 30.01.2017
@author adiM
"""

import traceback
from hangman.controllers.game_controller import GameController
from hangman.controllers.sentence_controller import SentenceController
from hangman.domain.validators import SentenceValidator
from hangman.repositories.file_repository import SentenceFileRepository
from hangman.repositories.sentence_repository import SentenceRepository
from hangman.ui.console import Console

if __name__ == '__main__':
    print("Hangman v1.0")

    try:
        sentence_repository = SentenceFileRepository(SentenceValidator, "../../data/sentences.txt")

        sentence_controller = SentenceController(sentence_repository)
        game_controller = GameController(sentence_repository)

        console = Console(sentence_controller,game_controller)

        console.run_app()
    except Exception:
        print("Error: ")
        traceback.print_exc()

    print("Bye!")