# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:25:20 2013

@author: yuankunluo
"""

def csvHandler(csv):
    """Handle all informations from csv.
    """
    data = readCsv(csv)
    # cut the head of csv out
    head = data[0]
    data = data[1:]
    # use a list to store usefull information
    result = []
    for tweets in data:
        time = tweets[3]
        tid = tweets[1]
        text = tweets[0]
        client = tweets[4]
        retweets = tweets[2]
        hashtags = tweets[5]
        result.append((time, tid,text,client,retweets,hashtags))
    result = dataBreaker(result)
    return result
    
    
    

def readCsv(c):
    """To read this csv data
    """
    import csv
    with open(c, "rb") as f:
        data = csv.reader(f,delimiter=';',quotechar='\"')
        result = []
        for row in data:
            result.append(row)
    return result
    

def dataBreaker(dataList):
    times = []
    hashtags = []
    words = []
    clients = []
    for data in dataList:
        time = data[0]
        word = data[2].split(" ")
        client = data[3]
        hashtag = data[5].split(" ")
        times.append(time)
        hashtags.extend(hashtag)
        words.extend(word)
        clients.append(client)
    return {u'times':times,u'hashtags': hashtags,
            u'words': words,'clients': clients}




    
