import random
guesses = []

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return str(secret_word).rstrip()

blank_list = list('-' * len(load_word()))

# For all following functions
# secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
# letters_guessed: list of letters that have been guessed so far.

def is_word_guessed(secret_word, letters_guessed):
    # returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
    # False otherwise
    secret_list = list(secret_word)
    result =  all(ltr in letters_guessed  for ltr in secret_list)
    if result:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    # returns: string, of letters and underscores.  For letters in the word that the user has
    # guessed correctly, the string should contain the letter at the correct position.  For letters
    # in the word that the user has not yet guessed, shown an - (hyphen) instead.
    secret_list = list(secret_word)
    guess_letter = input('Pick a letter in the alphabet: ').lower()
    # verify(guess_letter)
    guesses.append(guess_letter)
    if guess_letter in secret_list:
        index = secret_list.index(guess_letter)
        blank_list[index] = guess_letter
        print(''.join(blank_list))
        return True
    else:
        return False

def get_available_letters(letters_guessed):
    # returns: string, comprised of letters that represents what letters have not yet been guessed.
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    available = [letr for letr in alphabet if letr not in letters_guessed]
    return ''.join(available)

def spaceman(secret_word):
    # Starts up a game of Spaceman in the command line.
    # * At the start of the game, let the user know how many
    # letters the secretWord contains.
    # * Ask the user to guess one letter per round.
    # * The user should receive feedback immediately after each guess
    # about whether their guess appears in the computer's word.
    # * After each round, you should also display to the user the
    # partially guessed word so far, as well as letters that the
    # user has not yet guessed.
    print("There are {} letters in the secret word.".format(len(load_word())))
    wrong = 0
    while wrong < 7:
        if is_word_guessed(secret_word, guesses):
            print('Secret word confirmed. Launch aborted.')
            break
        elif get_guessed_word(secret_word, guesses) is True:
            print('Available letters: ' + get_available_letters(guesses))
        else:
            wrong += 1
            print('You have {} tries left'.format(7-wrong))
            if wrong == 7:
                print('Rocket Man Launched!')
                break

# print ()
# get_guessed_word(load_word(), guesses)
# is_word_guessed(load_word(), guesses)
# get_available_letters(guesses)
spaceman(load_word())
# print(load_word())
