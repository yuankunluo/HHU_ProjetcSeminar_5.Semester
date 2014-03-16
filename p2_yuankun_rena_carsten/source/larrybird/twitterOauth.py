# -*- coding: utf-8 -*-
"""We use the module to store all import credential for twitter Oauth.

Created on Wed Nov  6 19:57:39 2013

.. moduleauthor:: YuankunLUO <Yuankun.Luo@hhu.de>


"""
def getApi():
    """Use tweepy to handle the creepy but lovly twitter Oauth system,
    then return a api instance to continue our work.
    
    :param name: No param.
    :type name: None.
    :param state: None.
    :returns:  tweppy.Api instance 
    """ 
    import tweepy
    # creating an OAuthHandler instance
    auth = tweepy.OAuthHandler('2isZanDsKimDcBLMcHg',
                           'PoIxTGCUyrTxcdughdiIjaffVKrFuLnQf2QTp5aS7M')
#    try:
#        redirect_url = auth.get_authorization_url()
#    except tweepy.TweepError:
#        print 'Error! Failed to get request token.'
    auth.set_access_token('390104604-DOmwvmszefTMFIFWYe9sdM73NSuQ4HDYe6gRRmbh',
                      'HWg95QP0IKR5zoLhZ1qgqITOVaLPNzbSjP9JnrG2NOGfZ')
    api = tweepy.API(auth)
    return api