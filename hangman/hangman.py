from sys import argv
import numpy as np


class Hangman:
    MAX_MISTAKES = 5

    def __init__(self):
        self.word = None
        self.letters = set()
        self.mistakes = 0

    def choose_word(self, file_name='vocab.txt'):
        with open(file_name, 'r') as file:
            self.word = np.random.choice(file.readlines()).strip()

    def letter_checker(self, letter):
        return (
            len(letter) != 1 or not
            letter.isalpha() or
            letter in self.letters
        )

    def add_letter(self, letter):
        self.letters.add(letter)

    def process_letter(self, letter):
        if letter in self.word:
            print('Hit!')
        else:
            self.mistakes += 1
            print('Missed, mistake {} out of {}.'.format(
                self.mistakes, self.MAX_MISTAKES
            ))
        return self.mistakes

    def final_decision(self):
        if self.mistakes >= self.MAX_MISTAKES:
            print('You lost!')
            return True

        print('The word:', ''.join([
            l if l in self.letters else '*' for l in self.word
        ]))
        if {l for l in self.word}.issubset(self.letters):
            print('You won!')
            return True

        return False


def main(vocab_path):
    hangman = Hangman()
    hangman.choose_word(vocab_path)

    while True:
        print('Guess a letter:')
        letter = input().lower()
        if hangman.letter_checker(letter):
            continue

        hangman.add_letter(letter)
        hangman.process_letter(letter)
        if hangman.final_decision():
            break


if __name__ == '__main__':
    main(argv[1])
