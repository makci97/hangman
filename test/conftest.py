import pytest
from hangman.hangman import Hangman


@pytest.fixture
def prepare_hangman():
    hangman = Hangman()
    hangman.word = 'hello'
    return hangman
