# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 20:54:23 2019

@author: JFK3
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in lettersGuessed:
        if letter in secretWord:
            secretWord.remove(letter)
    if secretWord == '':
        return True
    else:
        return False