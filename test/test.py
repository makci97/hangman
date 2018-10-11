def test_letter_checker(prepare_hangman):
    letter = 'a'
    assert prepare_hangman.letter_checker(letter) is False
    letter = '&'
    assert prepare_hangman.letter_checker(letter) is True
    letter = 'aa'
    assert prepare_hangman.letter_checker(letter) is True


def test_add_letter(prepare_hangman):
    letter = 'a'
    prepare_hangman.add_letter(letter)
    assert prepare_hangman.letters == {'a'}
    letter = 'a'
    prepare_hangman.add_letter(letter)
    assert prepare_hangman.letters == {'a'}
    letter = 'b'
    prepare_hangman.add_letter(letter)
    assert prepare_hangman.letters == {'a', 'b'}


def test_process_letter(prepare_hangman):
    letter = 'h'
    assert prepare_hangman.process_letter(letter) == 0
    letter = 'a'
    assert prepare_hangman.process_letter(letter) == 1
