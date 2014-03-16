def makeBarPlot(inputDict,title,rank = 10,ylael = 'Anzhal'):
    # make figure
    result = {}
    from collections import OrderedDict
    result = OrderedDict(inputDict.items()[:rank])
    y = result.values()
    n = len(y)
    ind = range(n)
    labels = result.keys()
    from matplotlib import pyplot as p
    p.figure(figsize = (10,8), dpi=300, edgecolor = 'y')
    p.bar(ind, y, facecolor='blue',align='center', ecolor='r')
    p.title(title)
    p.xticks(ind, labels, rotation=70)
    p.savefig(title + ".png")
    p.show()

# http://scienceoss.com/bar-plot-with-custom-axis-labels/
