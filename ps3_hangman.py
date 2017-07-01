# Hangman game

# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
    if len(secretWord) == count:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    aStr = ''
    for i in secretWord:
        if i in lettersGuessed:
            aStr += i
        else:
            aStr += '_ '
    return aStr


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    aStr = ''
    for i in string.ascii_lowercase:
        if not i in lettersGuessed:
            aStr += i
    return aStr

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    if len(secretWord) > 1:
        print("I'm thinking of a word that is",len(secretWord),"letters long.")
    else:
        print("I'm thinking of a word that is",len(secretWord),"letter long.")
    print("------------")
    numGuess = 8
    lettersGuessed = []
    while numGuess > 0:
        if numGuess > 1:
            print("You have", numGuess ,"guesses left.")
        else:
            print("You have", numGuess ,"guess left.")
        print("Available Letters: ", end='')
        print(getAvailableLetters(lettersGuessed))
        temp = input("Please guess a letter: ").lower()
        if temp in lettersGuessed:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(temp)
            if temp in secretWord:
                print("Good guess:",getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed))
                numGuess -= 1
        print("------------")
        if isWordGuessed(secretWord, lettersGuessed):
            break
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was",secretWord+'.')

secretWord = chooseWord(wordlist)
hangman(secretWord)
