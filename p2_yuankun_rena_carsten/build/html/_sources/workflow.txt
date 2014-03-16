What can our programm do? (Programm workflow)
==============================

@Yuankun

This programm starts with module ***main.py***, all modules are in the package larrybird.

Start
----------------
main.start() function is the door of our project. It asks user to input a twitter (screenname).
After get the input twitter account, this programm automatcially downloads all tweets of this user,
stores this raw_data in disk. Then extracting all usefull data we need. At last, it generates 5 Diagramms for this account.




start() function are listed in blow:
::

	def start():
		"""To start the programm.
		
		:param None: No parameter asked
		:type None: None type
		:returns: None
		"""
		api = twitterOauth.getApi()
		twitterAccount = raw_input("Please give the account of twitter (screenname) ")
		getalltweets.getAllTweets(api, twitterAccount)
		inputData = twitterAccount
		result = computation.computeAll("data/"+ inputData + ".db")
		makePicture.makeAllPicture(result)
		return result

Get Tweets
--------------
As you can see, if first call the getApt() function in twitterOauth.py module.
After calling that, the api instance was returned. The api is like a key to the door of twitter, 
but with our Oauthority this key was paged with our application's tokens.

Store data
---------------
Then the programm asks user to input the twitter so it can collection tweets.
This step calls the ***getAllTweets()*** function in getalltweets.py module.
This function use the api and the inputed account to download all statuses of this twitter.
It stores this raw data in /data directory with filename suffix _raw.db

CLean data
---------------
In getalltweets.py module, after downloading we call a function ***extractUsefulInfo(alltweets)*** to 
extract for us meaningful data. For this little project, they are:
 
	* status (as String) --> for words statistic
	* created_at (as data.time object) --> for time analyse
	* hashtags (as list of string) --> for hashingtags ranking
	* source (as list of string) --> for client analyse
	
These meaningful data will be stored also in /data folder with filename suffix .db
	
Computation
----------------------
After cleaning data, this programm comes to ***computation.py*** module.
This module is maybe the most difficlut part for us. Really, why do you aks so many from us?
For God sake!

The complex part is in words statistic. Hier we try to use ***NLTK*** package.
NLTK is a very powerful NLP package, we just use two little tools from it.
	* reRextokenizer: use this to split the tweets sentenc into words, this dose better as simply use str.split(" ")
	* stopWorsSet: we retrieve a set of english stopwords to refine our computation
	
Our members has problem with the data.time object. So for this part, we dont use that package.

The result will be stored in /data foldre with filename suffix _result.db

Mathplotlib Plot
----------------------
All ploting things was written in this ***makePicture,py*** module.

The last step's result ist a dict object, like {'xxx_freqOfxxx': {xxx:xxx}}.
For detail please read code documentation.

There are three main functions in this module:

	* sortDict --> just for sorting Dict with ***OrderedDict*** datatype, because python dict can not be sorted.
	* makeBar --> plot a bar diagramm for one result, such like a bar for wordsfrequence of Lady GAGA.
	* makeCompBar --> plot a bar diagramm with two bars in it, to show the diffrerece of two twitter account.
	
Then we have in this module also some shortcut function, so that we can ust input result from last step automatically generate all plot and store them in /image folder.

Over
---------------------
That's all.

I hope next time, we have less work.
Please. The weise man make other man's life easy!

Team of Y,R,C 
