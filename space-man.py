import random
import re
guessed_list = []

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
        # '''
        # secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
        # lettersGuessed: list of letters that have been guessed so far.
        # returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
        # False otherwise
        # '''

        # FILL IN YOUR CODE HERE...
    guessed_list.append(letters_guessed)
    for letter in guessed_list:
        if letter in secret_word:
            return True
        else:
            return False

def get_guessed_word(secret_word, letters_guessed):
    # '''
    # secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    # lettersGuessed: list of letters that have been guessed so far.
    # returns: string, of letters and underscores.  For letters in the word that the user has
    # guessed correctly, the string should contain the letter at the correct position.  For letters
    # in the word that the user has not yet guessed, shown an _ (underscore) instead.
    # '''
    # FILL IN YOUR CODE HERE...
    check_guessed_list = is_word_guessed(secret_word, letters_guessed)
    if check_guessed_list == True:
        index = cross_check(secret_word,letters_guessed)
        for letter in secret_word:
            secret_word[index] = letters_guessed
    else:
        for letter in secret_word:
            index != index
            secret_word[index] = '_'
    return str(secret_word)


def cross_check (secret_word, letters_guessed):
    index = 0
    while index < len(secret_word):
        index = secret_word.find(str(letters_guessed), index)
        if index == -1:
            break
            return index
            index += 1



def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have nyet been guessed.
    '''




def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
    letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
    partially guessed word so far, as well as letters that the
    user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...

def test():
    secret_word = load_word()
    guess = 'a'
    print(secret_word)
    print(is_word_guessed(secret_word, guess))
    print(get_guessed_word(secret_word, guess))

test()
    # spaceman(load_word())
