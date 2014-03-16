# -*- coding: utf-8 -*-

import pickle
import re

def co_authorsAndYears(inputData, author = None):
    """Compute the co-author freq, publications year's freq
    from a given data, that a downloaded data
    resulted from datadownloader.py module.
    
    :param inputData: The .db file name under data folder
    :type inputData: String
    :returns: A List of 
    """
    inputR = None
    coauthor = []
    years = []
    if isinstance(inputData,str):
        with open(inputData,"rb") as f:
            inputR = pickle.load(f)
    else:
        inputR = inputData
    for doc in inputR:
        year = doc[u'year']
        authors = makeNamesTuple(doc['authors'])        
        years.append(year)
        coauthor.extend(authors)
    # compute frequnce
    coauthor = computeNameFreq(coauthor)
    years = computeFreq(years)
    # sort dict object order by value
    coauthor = sortDict(coauthor)
    years = sortDict(years)
    # delete the first author
    firstkey = coauthor.keys()[0]
    coauthor.pop(firstkey)
    author = firstkey[0] + "_" + firstkey[1]
    author = author.replace(" ","_")
    # make a dict of {"Name":Count}
    result = {}
    for key in coauthor.keys():
        name = key[0] +  " " + key[1]
        result[name] = coauthor[key]
    result = sortDict(result)
    with open("data/"+ author + "_coauthor.db","wb") as f:
        pickle.dump(result, f)
    print(author + "_coauthor.db was stored.")
    with open("data/" + author + "_years.db","wb") as f:
        pickle.dump(years, f)
    print("years of [ "+ author + " ] was stored!")    
    return result, years



def makesureCoauthor(authorname, authorList):
    """A function to make sure that the computed co-authors are
    true co-authors of a given author.
    
    :param authorname: A given author name
    :type authorname: A String
    :param authorList: A list of authors **nameletter**
    :type authorList: A List of string
    :returns: True if ok, otherwise False
    """
    if authorname in authorList:
        return True
    else:
        return False
    
def computeTopPopPaperInMag(paperList, topn = 10):
    """This function computes the top n **default n = 10** papers
    in a given paperList, which is the result of calling \
    datadownloader.popPapersInMag()
    function. 
    It return the top n element as list of tuple of (title, number)
    
    :param paperList: A list of tuples, which is a result of \
    datadownloader.popPapersInMag()
    :type paperList: A List
    :param topn: A ranking number
    :type topn: Integer
    :returns: A list of tuple of (title, readernumber)
    """
    if isinstance(paperList, str):
        with open(paperList, "rb") as f:
            paperList = pickle.load(f)
    paperList.sort(key=lambda tup: tup[0], reverse= True)
    paperList = paperList[:topn]
    result = []
    mag = paperList[0][2].replace(" ","_")    
    for paper in paperList:
        reader = paper[0]
        title = paper[3]
        result.append((title, reader))
    result = listtodict(result)
    with open("data/top_"+str(topn)+"_pop_papers_in_"+ mag+".db", 'wb') as f:
        pickle.dump(result, f)
    print("top%s__pop_papers_in_%s.db was stored."%(topn,mag))
    return result
    

def computeFreq(inputList, resultDict=None ):
    """A function to compute normal freq
    
    :param resultDict: A input Dict
    :type resultDict: Dict
    :param inputList: A input List
    :type inputList: A List
    :returns: A dict
    """
    if resultDict:
        result = resultDict
    else:
        result = {}
    for ele in inputList:
        if ele not in result.keys():
            result[ele] = 1
        else:
            result[ele] = result[ele] + 1
    return result

def computeNameFreq(inputList, resultDict = None):
    """A special function to compute authors' names frequence
    
    :param resultDict: A input Dict
    :type resultDict: Dict
    :param inputList: A input List **in form (forename, surname, nameletter)**
    :type inputList: A List
    :returns: A dict
    """
    if resultDict:
        result = resultDict
    else:
        result = {}
    nameletter = {}
    for ele in inputList:
        if ele[2] not in nameletter.keys():
            result[ele] = 1
            nameletter[ele[2]] = (ele,1)
        else:
            value = nameletter[ele[2]][1]
            key = nameletter[ele[2]][0]
            result[key] = value + 1
            nameletter[ele[2]] = (key, value + 1)
    return result
    
    
def makeNamesTuple(inputList):
    """Get the (forename, surname) tuple for quickly computation
    
    .. warning:: Due to the confusion in authors' names, 
        EG: the confusion between \
        'Wolfgang G Stock' and 'Wolfgang G.Stock'
        Hier we use **re** package to extract the letters in \
        authors name.
        If all the lettes of two names are the same, then they both \
        were computed to one author.
    
    :param inputList: A list of authors
    :type inputList: List
    :returns:  a List of tuples of (forename, surname, lettersofname)
    """
    result = []
    for nameD in inputList:
        forename = nameD['forename']
        surename = nameD['surname']
        nameletters = str(forename +  surename).lower()
        letterList = re.findall(r'\w*', nameletters)
        nameletters = "".join(letterList)
        result.append((forename, surename,nameletters))
    return result
        


def sortDict(inputDict, rank= None, n=1):
    """Sort the inputDict.
    
    :param inputDict: the Dict to sort
    :type inputDict: dict
    :param rank: A number to indicate how many items will be ranked
    :type rank: Int
    :return: OrderedDict
    """
    # first sort this input dict
    from collections import OrderedDict
    ranking = OrderedDict(sorted(inputDict.items(), key=lambda t: t[n]))
    items = ranking.items()
    items.reverse()
    ranking = OrderedDict(items)
    if rank :
        ranking = OrderedDict(ranking.items()[:rank])
    return ranking

def listtodict(inputList):
    """Covert a list to a dict.
    
    :param inputList: A list object of tuple (key,value)
    :type inputList: A list.
    :returns: a dict of {key, value}
    """
    result = {}
    for e in inputList:
        result[e[0]] = e[1]
    return result
        
        
        
