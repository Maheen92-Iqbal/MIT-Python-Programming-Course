# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "D:\python\MIT Program\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings 
    wordlist = line.split() #splitting lines into individual words
    print "  ", len(wordlist), "words loaded."
    
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
    
    store = ''
    
    for i in secretWord:
        
        if i in lettersGuessed:
            
            store = store + str(i)

    if store == secretWord:
        
        return True
        
    else:
        
        return False

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE.
    
    store = ''
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in letters:
               
         if i not in lettersGuessed:
         
            store = store + str(i)
          
    return store

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    store = ''
    
    for i in secretWord:
        
        if i in lettersGuessed:
            
            store = store + str(i)
        else:
            
            store = store + ' _ '
            
    return store

   
def hangman(secretWord):
    
    lettersGuessed = []
        
    guess = 8
    
    print 'Welcome to the game Hangman!'
    
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    
    while guess > 0:

       print '__________________________'
       
       print 'you have ' + str(guess) + ' guesses left '
       
       print 'Available letters: ' + str(getAvailableLetters(lettersGuessed))
       
       letters = raw_input('Please guess a letter: ')
       
       if letters in lettersGuessed:
           
           print 'Try Again as this letter has been guessed: ' + str(getGuessedWord(secretWord, lettersGuessed))
           
       
       elif letters not in secretWord:
           
           lettersGuessed.append(letters) 
           
           print 'Try Again that letter is not in the word: ' + str(getGuessedWord(secretWord, lettersGuessed))
           
       else:
            
           lettersGuessed.append(letters) 
       
           print 'Good Guess: ' + str(getGuessedWord(secretWord, lettersGuessed))
           
       if isWordGuessed(secretWord, lettersGuessed) == True:
           
           print 'Congratulations....You have Won the game!! '
           
           break
           
       guess = guess - 1
       
    if isWordGuessed(secretWord, lettersGuessed) == False:
        
       print '_________________________'
    
       print 'OOps you are out of guesses...lets try again!!!! '
       
       print 'The Word was ' + str(secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)