====
Documentation
====

----------
Module
----------

interbuild modules in python::

	import re
	import random
	import urllib2
	import os
	import time


- re 		= rgular expression
- random 	= to create random numbers
- urllib2	= for the text
- os 		= to clean the screen

----------
Functions
----------

main function::
	

	def initialGame():
		wordsList = makeWordsList()
		#print(wordsList[:10])
    	if askTOStart():
			startGame(wordsList)
			

wordsList::

	def wordsList():
		"""
		try-except-module is important, because of the nltk
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
