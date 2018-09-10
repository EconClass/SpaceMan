import space_man.py

def test():
    secret_word = load_word()
    print(secret_word)
    print(is_word_guessed(secret_word, guesses))
    print(get_guessed_word(secret_word, guesses))

test()
