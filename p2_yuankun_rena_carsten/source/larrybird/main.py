# -*- coding: utf-8 -*-
"""The main module to start this project.
Created on Wed Nov  6 19:57:49 2013

The workflow of this programm
-----
    
        1.  ask the twitter name (screen)
        2.  download the raw twitter data from twitter.com
        3.  extract our useful data fro raw _data
        4.  store this two data locally. (raw_data and clean data)
        5.  compute the frequence
        6.  store this compute result data locally (xxx_result.db)
        7.  use the result data to make pictures

.. moduleauthor:: YuankunLUO <Yuankun.Luo@hhu.de>
"""

import getalltweets
import computation
import makePicture
import twitterOauth

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
    
    

        

    
    