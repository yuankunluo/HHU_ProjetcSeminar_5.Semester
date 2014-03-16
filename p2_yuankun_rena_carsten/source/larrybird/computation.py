# -*- coding: utf-8 -*-
"""We use the module to compute all computational work for our collected data.

What to do
----

    1. Anzahl je Jahr, Monat, Tag, etc. (Analyse mit Hilfe des datetime-Moduls)
    2. Menge und Häufigkeit der verwendeten Wörter
    3. Menge und Häufigkeit der verwendeten Hashtags
    4. Menge und Häufigkeit der verwendeten Twitter-Clients
    
How
----
    we use tree functions to do this computation, every function use the clean data,
that we collected as input, then output something for matloplib.

Important:
----
    1. Every output data is in form of dict and stored with pickle in local.
    2. **NLTK** was used to clean stopwords and toknizer sentences.
    
Created on Wed Nov  6 19:57:39 2013


"""

def computeTime(inputData):
    """Tweets selected by year, month and day.
    Use the cleanded data from the getallweets.py module, this function loads
    the data and compute the frequrence for days, months and years.
    Use tree dicts to store the output with pickle into locale storage for makePicture.py.
    
    :param inputData: The name of the clean data (list objects).
    :type inputData: String
    :returns:  A tuple, whose elements are the dicts of years, months, days. 
    """
    
    import pickle
    data = None
    with open(inputData, "rb") as f:
        data = pickle.load(f)
    
    years = {}
    months = {}
    days = {}
    
    for tweet in data:
        year = tweet[3].year
        month = tweet[3].month
        day = tweet[3].day
        # Strings
        year = str(year)
        month = str(month)
        if len(month) == 1:
            month = "0" + month
        month = str(year) + month
        day = str(day)
        if len(day) == 1:
            day = "0" + day
        day = month + day
        if year in years.keys():
            altvalue = years[year]
            years[year] = altvalue + 1
        else:
            years[year] = 1
        if month in months.keys():
            altvalue = months[month]
            months[month] = altvalue + 1
        else:
            months[month] = 1
        if day in days.keys():
            altvalue = days[day]
            days[day] = altvalue + 1
        else:
            days[day] = 1
            
#    with open("data/"+ inputData + "_FreqOfyear.db", "wb") as f:
#        pickle.dump(years, f)
#    print(inputData + "_FreuOfYear.db was stored!")
#    
#    with open("data/"+ inputData + "_FreqOfmonth.db", "wb") as f:
#        pickle.dump(months, f)
#    print(inputData + "_FreuOfmonth.db was stored!")
#    
#    with open("data/"+ inputData + "_FreqOfday.db", "wb") as f:
#        pickle.dump(days, f)
#    print("data/"+ inputData + "_FreuOfday.db was stored!")
    
    return (years, months, days)
    
    
    

def computeFreqOfWords(inputData):
    """Computes the frequence of words used.
    Then returns a dict as output and stores the result dict in a local data.
    Try to import **NLTK** package to throw out those stop-word, then we can get more intressting data.   
    And use NLTK to tokenize words, and clean the shorturl or something not import.
    
    .. Note:: Not every pc has NLTK, in this function if NLTK was not successful imported,we just compute word frequence over raw inputdata.
    
    :param inputData: The name of the clean data (list objects).
    :type inputData: String
    :returns:  A dict, whose key is the word and value is integer. 
    """
    import pickle
    data = None
    result = {}
    wordlist = []
    with open(inputData,"rb") as w:
        data = pickle.load(w)
    for t in data:
        sent = t[1]
        words = sent.split(" ")
        try:
            import nltk
            from nltk.tokenize import RegexpTokenizer
            stopWords = set(nltk.corpus.stopwords.words( 'english' ))
            tokenizer = RegexpTokenizer(r'\w+')
            tokenWords = tokenizer.tokenize(sent)
            networds = set(["http", "co","i"])
            words = list(set(tokenWords) - stopWords-networds)
        except:
            continue
        finally:
            wordlist.extend(words)
    for word in wordlist:
        if len(word) < 3:
            wordlist.remove(word)
    for word in wordlist:
        if word in result.keys():
            result[word] = result[word] + 1
        else:
            result[word] = 1
#    with open("data/"+ inputData + "_FreqOfWords.db","wb") as f:
#        pickle.dump(result,f)
    return result
    
 
        
    

def computeFreqOfHashtags(inputData):
    """Computes the frequence of hashtags used.
    Then returns a dict as output and stores the result dict in a local data.
    
    :param inputData: The name of the clean data (list objects).
    :type inputData: String
    :returns:  A dict, whose key is the hashtag and value ist integer. 
    """
    import pickle
    with open(inputData,"rb") as r:
        data = pickle.load(r)
    hashlist = []
    result = {}
    for t in data:
        h  = t[2]
        hashlist.extend(h)
    for h in hashlist:
        if h in result:
            atv = result[h]
            result[h] = atv + 1
        else:
            result[h] = 1
#    with open("data/"+ inputData + "_FreqOfHashtags.db", "wb") as r:
#        pickle.dump(result, r)
#    print(inputData + "_FreqOfHashtags.db was stored!")
    return result

def computeFreqOfClient(inputData):
    """Compute die Frequence of Client, eg, iPad, web.
    Then return a dict as putput and store the result dict in a local data.
    
    :param inputData: The name of the clean data (list objects).
    :type inputData: String
    :returns:  A Dict, whoes key ist the client name and value ist interger. 
    """
    import pickle
    with open(inputData,"rb") as f:
        data = pickle.load(f)
    result = {}
    for tweet in data:
        client = tweet[4]
        if client in result.keys():
            result[client] = result[client] + 1
        else:
            result[client] = 1
#    with open("data/"+ inputData + "_FreqOfClient.db", "wb") as f:
#        pickle.dump(result, f)
#    print(inputData + "_FreuOfClient.db was stored!")
    return result

def computeAll(inputData):
    """A shorcut to call all functions in this module
    
    :param inputData: The name of the local data.
    :type inputData: String
    :returns: A dict of all informations
    """
    result = {}
    freqOfWords = computeFreqOfWords(inputData)
    freqOfHashtags = computeFreqOfHashtags(inputData)
    freqOfClients = computeFreqOfClient(inputData)
    freqOfTime = computeTime(inputData)
    freqOfYears, freqOfMonths , freqOfDays= freqOfTime[0], freqOfTime[1], freqOfTime[2]
    account = inputData[:-3]
    if account.startswith("data"):
        account = account[5:]
    result[account+"_"+"freqOfWords"] = freqOfWords
    result[account+"_"+"freqOfHashTags"] = freqOfHashtags
    result[account+"_"+"freqOfClients"] = freqOfClients
    result[account+"_"+"freqOfYears"] = freqOfYears
    result[account+"_"+"freqOfMonths"] = freqOfMonths
    result[account+"_"+"freqOfDays"] = freqOfDays
    
    with open(inputData[:-3] + "_result.db", "wb") as f:
        import pickle
        pickle.dump(result, f)
        print("Result stored under data folder.")
    return result
    
    


