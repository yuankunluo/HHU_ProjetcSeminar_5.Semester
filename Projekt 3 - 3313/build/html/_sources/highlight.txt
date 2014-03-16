HighLight
*****************************

makeNameTuple()
======================
    
    This funktion extracts the letter of a given authorname,
    exp: From "Wolfgan. G. Stock" it returns "wolfgangstock".
    
    We use this letter chain to compare with other authors.
    
    
    
    .. code-block:: python
    
        def makeNamesTuple(inputList):
            """Get the (forename, surname) tuple for quickly computation
            
            .. warning:: Due to the confusion in authors name, 
                EG: the confusion between 'Wolfgang G Stock' and 'Wolfgang G.Stock'
                Hier we use **re** package to extract the letters in authors name.
                If all the lettes of two names are the same, then they both was computed
                to one author.
            
            :param inputList: A list of authors
            :type inputList: List
            :returns:  a List of tuple of (forename, surname, lettersofname)
            """
            result = []
            for nameD in inputList:
                forename = nameD['forename']
                surename = nameD['surname']
                nameletters = str(forename +  surename).lower()
                letterList = re.findall(r'\w*', nameletters)
                nameletters = "".join(letterList)
                result.append((forename, surename,nameletters))
            return result



makeLineBar() 
======================

   This figure was created by the funkction diagramm.makeLineBar().
   The function gets a tuple as argument fsize.

    .. code-block:: python

        def makeLineBar(inputDict, filename, title, xlabel , output = \
        "image/", fsize = (15,20,5,2)):
            """A function to make a line bar plot. 
            
            :param inputDict: A inputData of {str:integer}
            :type inputDict: A Dict
            :param filename: The output picture's name.
            :type filename: String
            :param title: The title at top of this picture
            :type title: String
            :param xlabel: A short sentence at bottom of this pic.
            :type xlabel: String
            :param output: The folder path where our plot diagramms \
            were stored, **default** is the image folder.
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
            plt.barh(y_pos, performance, xerr=error, align='center', \
            alpha=0.4)
            plt.yticks(y_pos, y_keys, size='small')
            plt.xlabel(xlabel)
            plt.title(title)
            filename = filename.replace(" ", "_")
            plt.savefig(output + filename + ".png")
            plt.show()

