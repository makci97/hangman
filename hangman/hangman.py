import numpy as np

MAX_MISTAKES = 5


if __name__ == '__main__':
    with open('vocab.txt', 'r') as file:
        word = np.random.choice(file.readlines()).strip()

    letters = set()
    is_solved = False
    mistakes = 0
    while not is_solved and mistakes < MAX_MISTAKES:
        print('Guess a letter:')
        letter = input()
        if len(letter) != 1 or not letter.isalpha() or letter in letters:
            continue

        letters.add(letter)
        if letter in word:
            print('Hit!')
        else:
            mistakes += 1
            print('Missed, mistake {} out of {}.'.format(mistakes, MAX_MISTAKES))
            if mistakes >= MAX_MISTAKES:
                print('You lost!')
                break

        print('The word:', ''.join([l if l in letters else '*' for l in word]))
        if set([l for l in word]).issubset(letters):
            is_solved = True
            print('You won!')
            break
