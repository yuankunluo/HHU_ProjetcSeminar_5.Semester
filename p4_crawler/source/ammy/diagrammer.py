# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 7:46:18 2014
(code has to be placed in ammy folder)
Diagrammer plots simple charts from large data as images
by using limiting of x and y scales.


@author: alexh
"""


import operator
from dataanalyser import readCsv as Rcsv

from dataanalyser import sortDict

import matplotlib.pyplot as plt

from os import walk
fn=[]

results='./result/'

for (dirpath, dirnames, filenames) in walk(results):
  fn.extend(filenames)
  break


def barPlot(filename, title='default', xlabel='default'):
    #bar plot methods
    #read csv result file
    """
    filename: filename of csv result file
    captions: not working atm
    output: barplots in /diagramm/ folder
    """
    f=Rcsv(filename)
    values=[]
    keys=[]
    f=sorted(f, key=lambda x:x[1], reverse=True)
    f=[sublist[:2] for sublist in f[:10]]
    keys, values = [x.encode('utf-8') for x,y in f], [float(y.encode('utf-8')) for x,y in f]
    values=[int(x) for x in values]
    plt.ylim(0,len(values))    
    plt.xlim(0,10)
    plt.bar(range(len(values)), values, align='center')
    plt.xticks(range(len(keys)), keys, rotation=50, size="small")
    filename=filename.replace(".csv", "")
    filename=filename.replace("./result/", "")
    filename=filename.replace("100", "")
    plt.savefig("./diagramm/" + filename + ".png" )  
    plt.close()
    print "Image saved in ./diagramm folder..."
    
    
    
     
    

def crashplot(filelist):
    """
    input: list
    output: call rendering barPlot
    """
    for fi in filelist:
        fn=str(results+fi)
        barPlot(fn) 

crashplot(fn)    
print "Finish"   
    
 

  


 
