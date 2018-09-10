import random
import re
guesses = []

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return str(secret_word).lower()

def is_word_guessed(secret_word, letters_guessed):
    # secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    # lettersGuessed: list of letters that have been guessed so far.
    # returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
    # False otherwise
    secret_list = list(secret_word)
    if all(secret_list %in% letters_guessed):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    # secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    # lettersGuessed: list of letters that have been guessed so far.
    # returns: string, of letters and underscores.  For letters in the word that the user has
    # guessed correctly, the string should contain the letter at the correct position.  For letters
    # in the word that the user has not yet guessed, shown an _ (underscore) instead.
    secret_list = list(secret_word)
    for letter in secret_list:
        if letter in letters_guessed:
            return True
        else: letter = '_'
    return ''.join(secret_list)

def get_available_letters(letters_guessed):
    # lettersGuessed: list of letters that have been guessed so far
    # returns: string, comprised of letters that represents what letters have nyet been guessed.
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    return ''.join(alphabet.remove(letters_guessed))

def spaceman(secret_word):
    # secretWord: string, the secret word to guess.
    # Starts up a game of Spaceman in the command line.
    # * At the start of the game, let the user know how many
    # letters the secretWord contains.
    # * Ask the user to guess one letter per round.
    # * The user should receive feedback immediately after each guess
    # about whether their guess appears in the computer's word.
    # * After each round, you should also display to the user the
    # partially guessed word so far, as well as letters that the
    # user has not yet guessed.
    


def test():
    secret_word = load_word()
    print(secret_word)
    print(is_word_guessed(secret_word, guesses))
    print(get_guessed_word(secret_word, guesses))

# test()
spaceman(load_word())
