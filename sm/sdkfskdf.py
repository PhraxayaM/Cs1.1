import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    # FILL IN YOUR CODE HERE...
    for x in secretWord:
        if x not in lettersGuessed:
            return False
            return True
def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    string = ""
    for x in secretWord:
        if x in lettersGuessed:
            string += x
        else:
            string +='_'
    return string



def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    notGuessed = []
    for x in range(26):
        notGuessed += chr(x + ord('a'))

        for y in lettersGuessed:
            notGuessed.remove(y)

            string = ""
    for z in notGuessed:
        string += z
        return string



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
print("Welcome to the game Hangman!")
print("I am thinking of a word that is " + str(len(secretWord)) +" letters long")
print("-----------")
lettersGuessed = []
guesses = 7
    # while all the letters of secretWord are not yet in lettersGuessed and guesses left is more than 0
while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        # print first line
        print("You have " + str(guesses) +" guesses left")
        # print second line
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        # print third line
        # if user input a letter that has already been entered, reprompt for letter
while True:
    guessLetter = raw_input("Please guess a letter: ").lower()
    if guessLetter in lettersGuessed:
        print("You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        print("-----------")
        print("    You have " + str(guesses) +" guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
    else:
        break
    lettersGuessed += guessLetter
        # print last line
        # if correctly guessed secret word
    if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            print("Congratulations, you won!")
            break
        # else if the guess letter is in secret word
    elif guessLetter in secretWord:
        print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        print("-----------")
        # else the guess letter is not in secret word
else:
        print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        print("-----------")
        guesses -= 1
        # if ran out of guesses
if guesses == 0:
    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

#
secret_word = load_word()
spaceman(load_word())
