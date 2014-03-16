# -*- coding: utf-8 -*-
from compute import sortDict

def makeBarPlot(inputDict, filename, rank = 10,  title=None, ylabel = 'Count', output = "image/", fsize = (15,20,5,2)):
    """Plot the bar diagramm of the input dict.
    After the call of computation module's functions, \
    we have a inputDict as a result.
    This function uses this result to make a diagramm (plot) \
    then store the plot locally.
    ..Note: If the rank parameter is None, then output all data ranking.
    
    .. warning:  This function was reused from yuankun's project 2.
    
    :param inputDict: A dict of (key:value) paire.
    :type inputDict: Dict, the key is String, the value is interger
    :param rank: Indicate the top N (ranking), **default** is None
    :type rank: Integer
    :param output: The folder path where our plot diagramms were stored, **default** is the image folder.
    :type output: String
    :param fsize: The picture size
    :type fsize: A tuple of (width, length, xlimmax, xlimmin)
    :returns: None
    """
    
    # make figure
    y = inputDict.values()
    n = len(y)
    ind = range(n)
    filename = filename.replace(" ", "_")
    if n > 5:
        filename = filename + "TOP" + str(n)
    labels = inputDict.keys()
    
    from matplotlib import pyplot as p
    p.figure(figsize=(fsize(0),fsize(1)), dpi=300)
    p.xlim((fsize(2),fsize()))
    p.autoscale()
    p.bar(ind, y, facecolor='#777777',align='center', ecolor='black')
    p.title(filename)
    p.xticks(ind, labels, rotation=70, size='small')
    p.savefig(output + filename + ".png")
    p.show()

def makeLineBar(inputDict, filename, title, xlabel , output = "image/",\
 fsize = (15,20,5,2)):
    """A function to make a line bar plot. 
    
    :param inputDict: A inputData of {str:integer}
    :type inputDict: A Dict
    :param filename: The output picture's name.
    :type filename: String
    :param title: The title at top of this picture
    :type title: String
    :param xlabel: A short sentence at bottom of this pic.
    :type xlabel: String
    :param output: The folder path where our plot diagramms were \
    stored, **default** is the image folder.
    :type output: String
    :param fsize: The picture size
    :type fsize: A List of [width, length, xlimmax, xlimmin]
    :returns: None
    """
    import numpy as np
    import matplotlib.pyplot as plt
    data = sortDict(inputDict)
    data = [(k, v) for k, v in data.items()]
    y_keys = [k[0] for k in data ]
    y_pos = np.arange(len(y_keys))
    performance = [k[1] for k in data ]
    error = np.random.rand(len(y_keys))
    w, l, mi, ma = fsize[0], fsize[1], fsize[2],fsize[3]
    plt.figure(figsize=(w,l), dpi=300)
    plt.ylim((mi,ma))
    plt.autoscale()
    plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
    plt.yticks(y_pos, y_keys, size='small')
    plt.xlabel(xlabel)
    plt.title(title)
    filename = filename.replace(" ", "_")
    plt.savefig(output + filename + ".png")
    plt.show()
