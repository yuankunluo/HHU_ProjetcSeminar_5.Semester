# -*- coding: utf-8 -*-

import pickle

def top20TagsDownload(mendeley, catid = 6):
    """Download the top20 tags count for the giving catagory id.
    Then store the result local use the catagorie name.
    
    :parem mendeley: A mendeley client instance
    :type mendeley: mendeley_client.MendeleyClient
    :param cat: The categroie id, **Default is 6**
    :type cat: Integer
    :returns: a list of tuples, every tuple ist the (tagname, count) \
    pair.
    """
    cat = mendeley.categories()
    catslug = cat[catid-1][u'slug']
    catname = cat[catid-1][u'name']
    tags = mendeley.tag_stats(catid)
    result = []
    for ts in tags:
        name = ts[u'name']
        count = ts[u'count']
        result.append((name, count))
    with open("data/top_tags20_in" + catslug + ".db", "wb") as f:
        pickle.dump(result,f)
    print("Top 20 tags for categorie [ " + catname + " ] was stored!")
    return result

def papersInYears(mendeley, fromyear = 2013, toyear = 2013):
    """Download the year's account for a given timespace.
    Then store this information as a list of tuples.
    
    Use mendeley.search("year:YEAR")
    
    
    :param mendeley: A mendeley client instance
    :type mendeley: mendeley_client.MendeleyClient
    :param fromyear: The year for start counting
    :type fromyear: A four digit integer
    :param toyear: The end year for counting
    :type toyear: A four digit integer
    :returns: a List of tuple, (year:count)
    """
    m = mendeley
    result = []
    while fromyear <= toyear:
        year = fromyear
        s = m.search('year:'+str(year))
        count = s['total_pages']
        result.append((year,count))
        fromyear += 1
    
    with open("data/papers_"+str(fromyear) + "_to_" + str(toyear)+ ".db",
              "wb") as f:
        pickle.dump(result, f)
    print("Papers from " + str(fromyear) + " to " + str(toyear) + " was stroed.")
    return result

def authorsPapers(mendeley, author = "Wolfgang G. Stock"):
    """Search all papars for a given author's name
    
    :param mendeley: A mendeley client instance
    :type mendeley: mendeley_client.MendeleyClient
    :param author: A author name
    :type author: String
    :returns: a List of objects
    """
    m = mendeley
    s = m.search('author:"%s"'%(author))
    total_pages = s['total_pages']
    p = 0
    result = []
    while p < total_pages:
        s = m.search('author:"%s"'%(author),page = p)
        cpage = s[u'current_page']
        docs = s[u'documents']
        result.extend(docs)
        p += 1
        print("Page "+ cpage + "/" + str(total_pages) + " was computed!")
    author = author.replace(" ","_")
    with open("data/"+ author +".db", "wb") as f:
        pickle.dump(result,f)
        print("Data %s was stored!"%(author+ ".db"))
    return result
        

def popPaperInMag(mendeley, paperList):
    """After calling papersInMag() function we get all papers in the \
    specifical magzine.
    Then we use this function to collect the reader nummer for ervery \
    papaer in the given paperlist.
    This fuction also return a list of tuple(uuid, title, readnumber).
    
    :param mendeley: A mendeley client instance
    :type mendeley: mendeley_client.MendeleyClient
    :param paperList: a List of tuple resulted after papaerInMag() \
    function's calling.
    :type paperList: When a str, then this str indicates the file path.\
     Otherwise is a list object.
    :returns: A list of tuples of \
    (readers, title, mag, year, uuid, tags)
    """
    m = mendeley
    result = []
    if isinstance(paperList, str):
        with open(paperList, 'rb') as f:
            papers = pickle.load(f)
    else:
        papers = paperList
    mag = None
    count = 1
    for paper in papers:
        uuid = paper[0]
        mag = paper[4]
        title = paper[2]
        year = paper[1]
        # search for papers details
        details = m.details(uuid)
        readers = details[u'stats'][u'readers']
        tags = details['tags']
        result.append((readers, title, mag, year, uuid, tags))
        print(str(count) +"/" + str(len(paperList)) + \
        "was detailed gecheked.")
        count += 1
    with open("data/popPapers_in_"+ mag + ".db",'wb') as f:
        pickle.dump(result, f)
        print("data/popPapers_in_"+ mag + ".db was stored!")
    return result


def papersInMag(mendeley, mag = 'Nature'):
    """Search for a given mag, then collect papers in this mag.
    
    .. warning:: Due the limit of this API max 500 / hour. \
        This funktion collects infomations **only** \
        in the fist 100 pages. 
        Or onle collects max 500 results.
    
    
    :param mendeley: A mendeley client instance
    :type mendeley: mendeley_client.MendeleyClient
    :param topn: A Interger indicate ranking item
    :type topn: A Interger
    :param mag: A magzine name or a publication name
    :type mag: A string
    :returns: a list of tuple (uuid, title, year, url, \
    publication_outlet)
    """
    m = mendeley
    result = []
    s = m.search('published_in:Nature',page = 0)
    total_pages = s['total_pages']
    p = 0
    # maximal 100 seite werden angeruft or maximal only 500 results
    while p <= 10 or len(result) <= 500:
        s = m.search('published_in:Nature',page = p)
        cpage = s[u'current_page']
        try:
            docs = s[u'documents']
            for doc in docs:
                outlet = doc['publication_outlet']
                if outlet == mag:
                    uuid = doc[u'uuid']
                    title = doc[u'title']
                    year = doc[u'year']
                    url = doc[u'mendeley_url']
                    result.append((uuid,title,year,url,outlet))
            print(str(len(result)) + " papers was gefunden!")
            print("Page "+ cpage + "/" + str(total_pages) + \
            " was computed!")
        except:
            continue
        p += 1
    with open("data/papers_in_" + mag + ".db","wb") as f:
        pickle.dump(result,f)
        print("papers_in_%s.db was stored"%(mag))
    return result

def categoriesList(mendeley):
    """This function downloads the result that mendeley.categoreis() \
    returns.
    Then store this result in order this categorie id into a list of \
    tuple.
    Like [(catid, catname, catslug)]. We do this, because it is \
    convinient to checkt
    the catid in anothers functions. :)
    
    :param mendeley: A mendeley client instance
    :type mendeley: mendeley_client.MendeleyClient
    :returns: A list of categories
    """
    result =[]
    cats = mendeley.categories()
    for cat in cats:
        cid = cat[u'id']
        cname = cat[u'name']
        cslug = cat[u'slug']
        result.append((cid, cname, cslug))
    # sort this list in order by cid
    result.sort(key=lambda tup: tup[0], reverse= False)
    with open("data/cate_list.db",'wb') as f:
        pickle.dump(result,f)
    print("Categorie List was stored!")
    return result
    
    
             
def taggedInYear(mendeley, tag ='ontology', year = 2011):
    """This function search all taged by the gaven tag **default** \
    is ontology.
    Then filter these returned papers if it was publisched in 2011.
    Like all others functions, this one also stores the result locally
    
    .. warning:: Hier for every categorie we **only collect 5 returned \
     pages**. 
    
    :param mendeley: A mendeley client instance
    :type mendeley: mendeley_client.MendeleyClient
    :param tag: The tag, which was tagged a paper
    :type tag: String
    :param year: The specifics year
    :type year: Integer
    :returns: A Dict of {catid:(count, catname, catslug)}
    """
    m = mendeley
    result = {}
    presult = []
    with open("data/cate_list.db","rb") as f:
        catList = pickle.load(f)
    for cat in catList:
        cid = cat[0]
        cname = cat[1]
        cslug = cat[2]
        try:
            s = m.tagged(tag, cat = cid)
            cpage = s[u'current_page']
            tpage = s[u'total_pages']
            count = 0
            papers = []
            while cpage <= tpage and cpage < 5:
                s = m.tagged(tag, cat = cid, page = cpage)
                docs = s['documents']
                for doc in docs:
                    if doc[u'year'] == year:
                        papers.append(doc)
                        count += 1
                print("%s/%s pages under cat[ %s ] was computed"\
                %(cpage,tpage,cname))
                cpage += 1
            result[cname] = count
            # store detailed info for others use, i think
            presult.append((count, cname, cslug,papers))
            print("---- Categorie %s/%s [ %s ] was computed!"\
            %(str(cid), str(len(catList)),cname))
        except:
            print("Problem unter %s"%(cname))
            continue
    with open("data/taged_by_"+ tag + "in_year_"+ str(year) + \
    ".db","wb") as f:
        pickle.dump(result, f)
    with open("data/taged_paper_by_"+ tag + "in_year_"+ str(year) \
    + ".db","wb") as f:
        pickle.dump(presult,f)
    print("data/taged_by_"+ tag + "_in_year_"+ str(year) + \
    ".db was stored!")
    return result
        
def computeFreq(resultDict, inputList):
    """A function to compute freq
    
    :param resultDict: A input Dict
    :type resultDict: Dict
    :param inputList: A input List
    :type inputList: A List
    :returns: A dict
    """
    result = resultDict
    for ele in inputList:
        if ele not in result.keys():
            result[ele] = 1
        else:
            result[ele] = result[ele] + 1
    return result
    
        
        

    
