# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME =  "C:\\Users\\JFK3\\Documents\\words.txt"

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
    # FILL IN YOUR CODE HERE...
    secretList = list(secretWord)
    for letter in lettersGuessed: 
        if letter in secretList:
            secretList.remove(letter)
    if secretList == []:
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
    # FILL IN YOUR CODE HERE...
    '''
    secret list converts the secretWord into a list. 
    iterators over that list and if the letter is in that list and letter guessed
    removes that letter from letterGuessed. If the letter isn't in there then 
    returns _ 
    '''
    secretList = list(secretWord)
    for letter in secretList:
        if letter not in lettersGuessed:
            secretList[secretList.index(letter)] = '_ '
    return ''.join(secretList)

import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join([i for i in string.ascii_lowercase if i.lower() not in lettersGuessed])


def hangman(secretWord = chooseWord(wordlist)):
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
    # FILL IN YOUR CODE HERE...
    print ('Welcome to the game, Hangman!')
    print(' I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    print(secretWord)
    lettersGuessedsofar = [ ]
    mistakesmade = 0
    ans = secretWord
    while mistakesmade < 8:
        availableletters = getAvailableLetters(lettersGuessedsofar)
        print('')
        print('- - - -  - - - - -')
        print('You have ' + str(8 - mistakesmade) + ' guesses left')
        print(availableletters)
        lettersGuessedsofar.append(input('Please guess a letter'))
        print(lettersGuessedsofar)
        if lettersGuessedsofar[int(mistakesmade)] in secretWord:
            mistakesmade +=1
            print('Good Guess: ' + getGuessedWord(secretWord,lettersGuessedsofar))
        elif not lettersGuessedsofar[int(mistakesmade)] in availableletters:
            print('oops, youve already guessed that')
            lettersGuessedsofar.remove(int(mistakesmade))
        else:
            mistakesmade +=1
            print('Wrong Guess')
        if isWordGuessed(ans,lettersGuessedsofar):
            mistakesmade +=8
            print ('congrats, You won the game!')
    
    if not isWordGuessed(ans,lettersGuessedsofar):
        print('loser')


###### Leaving as is!!!  Only problem left is it lets you repeat guesses
        #### It won't remove it from the list for whatever reason. Good enoug for me:) proud of ya champ!!
                
hangman()






# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
