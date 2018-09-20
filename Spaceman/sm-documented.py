import random

def load_word():
    '''
    returns: str, from a random choice of the words.txt file
    '''

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the random word the user is trying to guess.  This is selected on line 9.
    letters_guessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    # FILL IN YOUR CODE HERE...
    for x in secret_word:
        if x not in letters_guessed:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the random word the user is trying to guess.  This is selected on line 9.
    letters_guessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    string = ""
    for x in secret_word:
        if x in letters_guessed:
            string += x
        else:
            string +='_'

    return string

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    notGuessed = []

    # add all letters in alphabet in notGuessed
    for x in range(26):
        notGuessed += chr(x + ord('a'))

    # then, remove the letters that are already gessed
    for y in letters_guessed:
        notGuessed.remove(y)

    # construct a string of all letters in notGuessed
    string = ""
    for z in notGuessed:
        string += z

    return string

def spaceman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secret_word contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) +" letters long")
    print("-----------")
    letters_guessed = []
    guesses = 7

    # while all the letters of secret_word are not yet in letters_guessed and guesses left is more than 0
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        # print first line
        print("You have " + str(guesses) +" guesses left")
        # print second line
        print("Available Letters: " + get_available_letters(letters_guessed))
        # print third line
        # if user input a letter that has already been entered, reprompt for letter

        # keep asking the user guesses until the user has either won, or ran out of guesses
        while True:
            guess_letter = input("Please guess a letter: ").lower()

            # check if the user has already guessed the given letter
            if guess_letter in letters_guessed:
                print("You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
                print("-----------")
                print("    You have " + str(guesses) +" guesses left")
                print("Available Letters: " + get_available_letters(letters_guessed))
            else:

                # add new guessed letter to list of previously guessed
                letters_guessed += guess_letter

                # did you win?
                if is_word_guessed(secret_word, letters_guessed):
                    print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------")
                    print("Congratulations, you won!")
                    break

                # did you guess a correct letter?
                elif guess_letter in secret_word:
                    print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------")

                # else, you guessed incorrectly
                else:
                    print("That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                    print("-----------")
                    guesses -= 1

                    # if ran out of guesses
                    if guesses == 0:
                        print("You ran out of guesses! The word was " + secret_word + ".")
                        break

    print("Game Over")

# run the program
secret_word = load_word()
spaceman(secret_word)
