# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:37:59 2013

"""

import re
import random
import urllib2
import os
import time

"""
====
Module
====

interbuild mudoles in python
----------

re = rgular expression

random = to create random numbers

urllib2 = for the text

os = to clean the screen
    - it s improtant for the game, that the terminal will be cleaned
"""

    

def intialGame():
    
"""
====
Functions
====

main function

"""
    wordsList = makeWordsList()
    #print(wordsList[:10])
    if askToStart():
        startGame(wordsList)



def makeWordsList(fileurl = 'http://www.gutenberg.org/cache/epub/11/pg11.txt', 
                language = 'english',
                minLength = 3):
"""
====
Wordlist
====
- this function creates a wordlist for the game
- it accepts 3 arguments:
    - a URL and a default file (alice in wonderland)
    - language
    - min length
    
----------
try and except
----------

it s improtant to use the "try and except-module" because not every computer can read nltk
    - without using nltk it could be difficult to get a "clean" list


- the language argument is just a default argument, in fact we could import every language
- create a stopwordlist
- save the "results" in stopwords
- regexpTookenizer to get a "clean"amount of words

- after import the programm reads a file (input.txt)

----------
finally
----------
- filter with arguments
    
    1. min length
    2. save in the variable "results" to create the dadabase for the words
    
"""
    try:
        import nltk
        from nltk.tokenize import RegexpTokenizer
        stopWords = set(nltk.corpus.stopwords.words( language ))
        f = urllib2.urlopen(fileurl)
        tokenizer = RegexpTokenizer(r'\w+')
        cleanWords = list(set(tokenizer.tokenize(f.read()))- stopWords)
    except ImportError :
        print("Error importing nltk, initial game from default txt.")    
        with open('input.txt') as f:
            txt = f.read()
            cleanWords = txt.split(" ")
    finally:
        result = [x for x in cleanWords if len(x) >= minLength]
    return result


def startGame(wordsList):
    
"""
====
start game
====
a function with the created wordlist as it s argument

"""
    
    targetWord = pickTarget(wordsList)
    #print(targetWord)
    guess(wordsList, targetWord)

    
    
def pickTarget(wordsList):
    index = random.randint(0,len(wordsList)-1)
    word = wordsList[index]
    return word
    
    
def guess(wordsList, targetWord):
    targetWord = targetWord.lower()
    targetWord = list(targetWord)
    returnWord = ['*' for w in targetWord]
    bingoTime = 0
    retryTime = 10
    history = []
    showAnswer = True
    while True:
        clear()
        makeTui(targetWord,bingoTime, returnWord, retryTime, history, showAnswer)
        inputLetter = askLetter().lower()
        if inputLetter == "222":
                showAnswer = True
                makeTui(targetWord,bingoTime, returnWord, retryTime, history, showAnswer)
                askForOneMoreTime(1,wordsList)
        for i in range(0, len(targetWord)):
            if inputLetter == targetWord[i]:
                returnWord[i] = inputLetter
        #print(returnWord)        
        if ''.join(returnWord) != ''.join(targetWord):
            history.append(inputLetter)
            retryTime -= 1
            if retryTime == 0:
                askForOneMoreTime(2, wordsList)
        if ''.join(returnWord) == ''.join(targetWord):
            askForOneMoreTime(1, wordsList)
        
        
        
        
    
            

def makeTui(targetWord, bingoTime, returnWord, retryTime, history, showAnswer):
    info = "{t}\n"
    
"""
====
Text user interface
====

- for a simple output on the screen

"""
    #info += "Hier ist your No. {bingoTime} word to guess: {s}"
    info += "\t [ {returnWord} ]\t{s}"
    info += "Your have {Time} chance to try. {s}"
    info += "Your history: [ {history} ] . {s}"
    if showAnswer:
        info += "The answer is [ {answer} ]. {s}"
    info += "{t}\n"
        
    print(info.format(s='\n',t='-'*50,
                      returnWord = ' '.join(returnWord),
                      #bingoTime = number + 1,
                      Time = retryTime,
                      answer = ''.join(targetWord),
                      history = ",".join(history)))


def askLetter():
    
"""
====
ask letter
====

- save in variable "inputLetter"

"""
    print("Enter [888] to exit game;[222] to showAnswer")
    inputLetter = raw_input("Please give a letter: ")
    if inputLetter == "888":
        exit()
    if inputLetter == "222":
        return "222"
    while not re.match("^[a-z]$", inputLetter):
        print("Error! Only one letters from a-z allowed!\n")
        inputLetter = askLetter()
    return inputLetter


def askToStart():
    
"""
====
Start game
====
simple function to ask to start the game

- variable "start"
- exit() is a python build-in function
    - is going to exit python
    
-if "true" the game will start and return to **startGame**

"""
    print("Welcome to our game!")
    start = raw_input("Please press anykey to start game,\nor input [exit] to quit: ")
    if start.lower == "exit":
        print("F**k, why dont you cantinue! I HATE YOU! TMF")
        exit()
    if len(start) > 0 :
        return True

    
def askForOneMoreTime(n, wordsList):
    
"""
====
timemodule
====
----------
1. if-loop
----------

if the user guessed right

----------
2. if-loop
----------

the user guessed worng and after waiting 2 sec.

"""
    if n == 1:
        print("Yeah! You guess right!")
        oneMoreTime = raw_input("Exit? Enter [Y] to exit or [N] to retry one more time: ").lower()
        if oneMoreTime in ['y','n']:
            if oneMoreTime == 'y':
                exit()
            if oneMoreTime == 'n':
                askForOneMoreTime(2, wordsList)
    if n == 2:
        print("Now wait for 2 secends skip to next word")
        time.sleep(2)
        startGame(wordsList)

        
        
        
        
        
        
def clear():
	import os
	os.system('cls' if os.name=='nt' else 'clear')


intialGame()
