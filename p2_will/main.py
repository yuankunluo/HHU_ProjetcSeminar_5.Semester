# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:57:56 2013

@author: yuankunluo
"""

import csvReader as cr
import tweepy_timeline_cursor as tc

def start(username):
    tc.collectTweets(username)
    result = cr.csvHandler(username + ".csv")
    return result