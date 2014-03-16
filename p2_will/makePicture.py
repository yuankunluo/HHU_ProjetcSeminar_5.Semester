# -*- coding: utf-8 -*-
"""Use **matplotlib** to generate pics.

"""

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

def makeBarPlot(inputDict, filename, rank = 10,  title=None, ylabel = 'Count'):
    """Plot the bar diagramm of the input dict.
    After call of computation module's functions, we have a inputDict als result.
    This function use this result to make diagramm (plot) then store the plot locally.
    ..Note: If the rank parameter is None, then output all data ranking.

    :param inputDict: A dict of (key:value) paire.
    :type inputDict: Dict, the key is String, the value is interger
    :param rank: Indicate the top N (ranking), **default** is None
    :type rank: Integer
    :param output: The folder path where our plot diagramms were stored, **default** is the image folder.
    :type output: String
    :returns: None
    """
    ranking = sortDict(inputDict, rank)
    # make figure
    y = ranking.values()
    n = len(y)
    ind = range(n)
    if n > 5:
        filename = filename + "TOP" + str(n)
    labels = ranking.keys()
    
    from matplotlib import pyplot as p
    p.figure(figsize = (10,8), dpi=300, edgecolor = 'black')
    p.bar(ind, y, facecolor='#777777',align='center', ecolor='black')
    p.title(filename)
    p.xticks(ind, labels, rotation=70)
    p.savefig(filename + ".png")
    p.show()
    
    
def makeCompareBar(inputDict1, inputDict2, 
                   fileName1, fileName2,
                   rank = 5, output="image/"):
    """This function use two InputDict as input parameter, then plot a two bars diagramm.
    
    :param inputDict1: The first inputDict.
    :type inputDict1: A dict object of items in form of (String,int)
    :param inputDict2: The second inputDict.
    :type inputDict2: A dict object of items in form of (String,int)
    :param fileName1: The name that appears as a part of the title of this diagramm
    :type fileName1: String.
    :param fileName2: The name that appears as a part of the title of this diagramm
    :type fileName2: String.
    :param rank: Indicate how many items will be showed (ranking for top N), **default is 5**
    :type ranak: int
    :param output: The directory , where the output png files will be stored locally
    :type output: String
    :returns: None
    """
    # first sort the two inputDict
    dict1 = sortDict(inputDict1, rank)
    dict2 = sortDict(inputDict2, rank)
    # then import the useful package
    import numpy as np
    import matplotlib.pyplot as plt
    # get the key/ values of two dicts
    keys_1 = dict1.keys()
    values_1 = dict1.values()
    keys_2 = dict2.keys()
    values_2 = dict2.values()
    # rank is the int that remembers how many ranking we need
    ind = np.arange(rank)
    # the width of the bars
    width = 0.35
    # make a figure and axies using plt
    fig, ax = plt.subplots()
    fig.set_dpi(500)
    fig.set_figheight(10)
    fig.set_figwidth(15)
    # use tha ax to build bar
    bar1 = ax.bar(ind, values_1, 
                  width, color='r')
    bar2 = ax.bar(ind+width, values_2, 
                  width,color='y')
    # add the label and title
    ax.set_ylabel('Count of tweets')
    ax.set_title( fileName1 +' vs ' + fileName2 + " TOP " + str(rank))
    # make the labels for x-axe
    #ax.set_xticks((ind+width)/2)
    xlabels = []
    for i in range(rank):
        xlabels.append(keys_1[i])
        xlabels.append(keys_2[i])
    #xlabels = tuple(xlabels)
    #ax.set_xticklabels( xlabels )
    # set the legend
    ax.legend( (bar1[0], bar2[0]), (fileName1, fileName2) )
    # define a function to attach some text labels
    def autolabel(rects, keys):
        i = 0
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')
            ax.text(rect.get_x()+rect.get_width()/2.,0,keys[i], 
                    ha='right', va='top', rotation= 75)
            i += 1
    autolabel(bar1,keys_1)
    autolabel(bar2,keys_2)
    plt.savefig(output + fileName1 + "_vs_" + fileName2 + ".png")
    plt.show()
    
    
def makeAllPicture(result):
    """A shortcut to make all bar diaagramms.
    
    :param result: The result data that stored locally after computation.py processing.
    :type result: Dict.
    :returns: None
    """
    for key, value in result.items():
        makeBarPlot(value, key)

def makeAllCompare(result1, result2):
    """A short to make all compare bar diagramms, using the module makePicture.py
    
    
    :param result1: The first result data that stored locally after computation.py processing.
    :type result: Dict.
    :param result2: The second result data that stored locally after computation.py processing.
    :type result: Dict.
    :returns: None
    """
    # first sort this input dict
    from collections import OrderedDict
    result1 = OrderedDict(sorted(result1.items(), key=lambda t: t[0]))
    result2 = OrderedDict(sorted(result2.items(), key=lambda t: t[0]))
    # get iterator for this two dict
    i1 = iter(result1)
    i2 = iter(result2)
    try:
        while True:
            k1 = next(i1)
            dict1 = result1[k1]
            k2 = next(i2)
            dict2 = result2[k2]
            if len(dict1.keys()) < 5 or len(dict2.keys()) < 5:
                continue
            makeCompareBar(dict1, dict2, k1, k2)
    except StopIteration:
        pass
    finally:
        del i1,i2
        



    
    
    
    
