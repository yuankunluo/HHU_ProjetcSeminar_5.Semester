# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:25:20 2013

@author: yuankunluo
"""

def csvToDict(csv):
    """Handle all informations from csv.
    """
    data = readCsv(csv)
    wordList = []
    sourceList = []
    timeList = []
    hashtagsList =[]
    for tweet in data:
        words = tweet[0].split(" ")
        source = tweet[1].split(" ")
        time = tweet[2][:10]
        time = time.split("-")
        time = "".join(time)
        hashtags = tweet[4].split(" ")
        wordList.extend(words)
        sourceList.extend(source)
        timeList.append(time)
        hashtagsList.extend(hashtags)
    # count
    wordD = countList(wordList)
    sourceD = countList(sourceList)
    timeD = countList(timeList)
    hashD = countList(hashtagsList)
    result = (wordD, sourceD, timeD,hashD)

    return result
    

def countList(li):
    result = {}
    for ele in li:
        if ele == "":
            continue
        if ele in result.keys():
            result[ele] = result[ele] + 1
        else:
            result[ele] = 1
    # sort
    result = sortDict(result)
    return result
    
def sortDict(inputDict):
    # first sort this input dict
    from collections import OrderedDict
    rs = OrderedDict(sorted(inputDict.items(), key=lambda t: t[1]))
    items = rs.items()
    items.reverse()
    rs = OrderedDict(items)
    rs = OrderedDict(rs.items())
    return rs
    

def readCsv(c):
    """To read this csv data
    """
    import csv
    with open(c, "rb") as f:
        data = csv.reader(f,delimiter=',',quotechar='\"')
        result = []
        for row in data:
            result.append(row)
    return result


    
