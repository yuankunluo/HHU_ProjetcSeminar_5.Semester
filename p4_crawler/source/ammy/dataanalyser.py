# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:39:12 2014

@author: yuankunluo
"""
import os
import nltk
import unicode_csv as ucsv
import pickle
import re as reg
import numpy

try:
    import datadownloader as dr
except:
    pass



def statistic(f,t):
    """Compute the numbers of somethings for a given years range.
    Read the file with name imdb_year.csv in data folder.
    
    :param f: From year
    :type f: Integer
    :param t: To year
    :type t: Integer
    :returns: A  list of (year:number)
    """
    something = {u'actors':11, 
            u'writers':6, 
            u'directors':9,
            u'genres':13,
            u'countries':5,
            u'languages':3,
            }
    data = readDataInRange(f,t,True,True)
    datalist = readDataInRange(f,t,False, False)
    bigres = {u'actors':[], 
            u'writers':[], 
            u'directors':[],
            u'genres':[],
            u'countries':[],
            u'languages':[]
            }
    for y in sorted(data.keys()):
        details = data[y]
        for key, value  in something.items():
            l = listToList([x[value] for x in details])
            bigres[key].extend(l)  
    # do top-n analyses
    top_n_produktiv_something_in_range(f,t,bigres)
    #
    for key, value in bigres.items():
        v = nltk.FreqDist(value)
        bigres[key] = len(v.keys())
    bigres["movies"] = len(datalist)
    rating = [float(x[1][2]) for x in datalist if float(x[1][2]) != 0]
    maxrating = numpy.max(rating)
    minrating = numpy.min(rating)
    bigres["average_rating"] = numpy.average(rating)
    bigres["max_rating"] = maxrating
    bigres["min_rating"]  = minrating
    runtime = [x[1][3] for x in datalist]
    p = reg.compile("\d+")
    runtime = [float(reg.match(p,x[1][3]).group(0)) for x in datalist if x[1][3] != "Unknown"]
    runtime_sum = numpy.sum(runtime)
    runtime_average = numpy.average(runtime)  
    runtime_min = numpy.min(runtime)
    runtime_max = numpy.max(runtime)
    bigres["runtime_sum"] = runtime_sum
    bigres["runtime_average"] = runtime_average
    bigres["runtime_min"] = runtime_min
    bigres["runtime_max"] = runtime_max
    if t == f:
        fn = "statistic_in_{f}".format(f=f)
    else:
        fn = "statistic_in_{f}_{t}".format(t=t, f=f)
    c = [(k, v) for (k,v) in bigres.items()]
    dr.tupleToCSV(c,"result/"+fn)
        

def top_n_produktiv_something_in_range(f,t,data,top=100):
    """Compute the top-N most produktiv something in one year.
    Something like writer, director, actor, genre, country, language.
    Just count the frequence of data.
    
    :param f: The given from year number
    :type f: Integer
    :param t: The given to year number
    :type t: Integer
    :param top: A indicater to speicifiy the ranking
    :type top: Integer
    :param dataDict: A dict of {something:list of string}
    :type dataDict: A dict
    :returns: A list of (something,numbers)
    """
    for key, v in data.items():
        result = []
        freq = sortDict((nltk.FreqDist(v)))
        for k in freq.keys()[:top+1]:
            if k.lower() == "n/a":
                continue
            result.append((k, freq[k]))
        if t == f:
            fn = "top_{n}_produktiv_{some}_{f}".format(n=top, some= key, f=f)
        else:
            fn = "top_{n}_produktiv_{some}_{f}_{t}".format(n=top, some= key, f=f,t=t)
        writeData(result, fn)
    
def top_n_keywords_in_range(t,f,top = 100):
    """Analyse the plot (story abstract) of movies,
    then count the key words (get rid of stopsswords).
    
    :param year: The given year
    :type year: Integer
    :param top: The number speicifies rangking
    :type top: Integer
    :returns: A list of tuple (keyword,count)
    """
    result = []
    data = readDataInRange(t,f,False, False)
    wlist = []
    for d in data:
        plot = d[1][7]
        words = cleanDoc(plot)
        wlist.extend(words)
    freq = nltk.FreqDist(wlist)
    freq = sortDict(freq)
    for k in freq.keys()[:top+1]:
        if k.lower() == "unknown":
            continue
        result.append((k, freq[k]))
    if t == f:
        fn = "top_{n}_{some}_{f}".format(n=top, some= "keywords", f=f)
    else:
        fn = "top_{n}_produktiv_{some}_{f}_{t}".format(n=top, some= "keywords", f=f,t=t)
    writeData(result, fn)

def best_n_rated_movie_in_range(f, t, top=100):
    """Use the imdb rating to compute the value of a director.
    
    :param f: from year
    :type f: Int
    :param t: to year
    :type t: Int
    :param top: A rank number
    :type top: Int
    :returns: A list of tuples (directorname, rating)
    """
    data = readDataInRange(f,t)
    data = [(x[1][1],float(x[1][2]),x[1][4]) for x in data if float(x[1][2]) > 0]
    dt = sorted(data, key = lambda t: t[1], reverse=True)[:top+1]
    if t == f:
        fn = "best_{n}_rated_movie_in_{f}".format(n=top, f=f)
    else:
        fn = "best_{n}_rated_movie_in_{f}_{t}".format(n=top, f=f,t=t)
    writeData(dt,fn)

def best_n_awarded_movies_in_range(f,t, award="o"):
    """Use the imdb rating to rank the movies, that won oscar award.
    
    :param f: from a year
    :type f: int
    :param t: to a year
    :type t: string
    :param award: The award : {o:oscar, g:golden_global
    :type award: String
    :returns: none
    """
    data = readDataInRange(f,t,True,False)
    award = award[0].lower()
    awards = {"o":"oscar","g":"golden globe"}
    result = []
    p = r"\d+.{a}".format(a=awards[award])
    p = reg.compile(p)
    for d in data:
        y = d[0]
        m = d[1]
        aw = m[14].lower()
        if reg.search(p,aw):
            r = reg.search(p,aw).group(0)
            r = r.split(" ")
            result.append((m[4], float(m[8]), int(r[0]),r[1],y, m[9],m[5],))
    result = sorted(result, key = lambda t : t[1], reverse = True)
    if t == f:
        fn = "best_{a}_movie_in_{f}".format(a=awards[award], f=f)
    else:
        fn = "best_{a}_rated_movie_in_{f}_{t}".format(a=awards[award], f=f,t=t) 
    writeData(result, fn)
    
        
        

#--------------- hlep functions ----------------------  

def readCsv(filename):
    """A short cut to read csv
    
    :param filename: CSV file
    :type filename: A string
    :returns: A list
    """
    data = []
    with open(filename, "rb") as f:
        raw = ucsv.UnicodeReader(f)
        for r in raw:
            data.append(r)
    return data

def sortDict(inputDict, rank= None):
    """Sort the inputDict.
    
    :param inputDict: the Dict to sort
    :type inputDict: dict
    :param rank: A number to indicate how many items will be ranked
    :type rank: Int
    :return: OrderedDict
    """
    # first sort this input dict
    from collections import OrderedDict
    ranking = OrderedDict(sorted(inputDict.items(), key=lambda t: t[1]))
    items = ranking.items()
    items.reverse()
    ranking = OrderedDict(items)
    if rank :
        ranking = OrderedDict(ranking.items()[:rank])
    return ranking
  
def cleanDoc(doc, language= "english"):
    """A help function to get the clean txt.
    
    :param doc: A processing text
    :type doc: String
    :param language: A language used to get the stoppswords corpus of nltk
    :type language: Sting
    :retuns: A list of words that was cleaned .
    """
    # get rid of stopwords
    stopset = set(nltk.corpus.stopwords.words(language))
    # just use word's stamm for caculation
    stemmer = nltk.PorterStemmer()
    tokens = nltk.tokenize.WordPunctTokenizer().tokenize(doc)
    clean = [token.lower() for token in tokens if token.lower() not in stopset and len(token) > 5]
    final = [stemmer.stem(word) for word in clean]
    return final

def readDataInRange(f, t, detail = False , rDict = False):
    """Read data in a given range .
    
    :param f: from year
    :type f: Int
    :param t: to year
    :type t: Int
    :param detail: if read the detailed data
    :type detail: Boolean
    :param rDict: Specify the return form as dict, default is False
    :type rDict: boolean
    :returns: A list of tuple (year,data)
    """
    if rDict:
        result = {}
    else:
        result = []
    path = os.path.dirname(os.path.abspath(__file__)) + "/data"
    if detail:
        path = path + "/datail"
    flist = os.listdir(path)
    flist = [x for x in flist if x.endswith(".csv")]
    for fn in flist:
        key = re.findall(r"\d",fn)
        key = [x for x in key]
        if len(key) != 4:
            continue
        key = "".join(key)
        key = int(key)
        if key in range(f,t+1):
            value = readCsv(path+"/"+fn)
            #print("key %s was readed."%(str(key)))
            if detail:
                value = value[1:]
            if rDict:
                result[str(key)] = value
            else:
                for v in value:
                    result.append((key, v))       
    return result

def writeData(data,fname):
    """Write a data into csv and pickle objec.
    
    :param data: The data to be wrote
    :type data: A list of tuple
    :param fname: A filename
    :type fname: String
    :returns: None
    """
    dr.tupleToCSV(data, "result/"+fname,None)
#==============================================================================
#     with open("result/"+fname,"wb") as f:
#         pickle.dump(data, f)
#==============================================================================

def listToList(l):
    """Short cut to help comput complex data
    """
    data = ",".join(l)
    data = data.split(",")
    data = [x.strip(" ") for x in data]
    return data




    
    

    
