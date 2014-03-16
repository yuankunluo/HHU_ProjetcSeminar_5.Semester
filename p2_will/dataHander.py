# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:41:36 2013

@author: yuankunluo
"""

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
        