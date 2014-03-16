# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:42:27 2013

@author: yuankunluo
"""
import pickle

def top20TagsDownload(mendeley, catid = 6):
    """Download the top20 tags count for the giving catagoreie id.
    Then store the result local use the catagorie name.
    
    :parem mendeley: A mendeley client instance
    :type mendeley: mendeley_client.MendeleyClient
    :param cat: The categroie id, **Default is 6**
    :type cat: Integer
    :returns : a list of tuples, every tuple ist the (tagname, count) pair.
    """
    cat = mendeley.categories()
    catslug = cat[catid][u'slug']
    tags = mendeley.tag_stats(catid)
    result = []
    for ts in tags:
        name = ts[u'name']
        count = ts[u'count']
        result.append((name, count))
    with open("data/" + catslug + ".db", "wb") as f:
        pickle.dump(result,f)
    return result
        

    