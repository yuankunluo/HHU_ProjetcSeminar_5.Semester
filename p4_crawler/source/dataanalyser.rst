Analysis Process
===========================

The analysis processes was done by the module **dataanalyser.py**.

This module reads all the downloaded data in Data folder, then use NLTK and others to analyse.


Keywords Analysis Process
---------------------

For keywords it uese NLTK to get the stemms of words, then get the frequence ranking with nltk.FreqDist.

.. code-block:: python
   :emphasize-lines: 12,26,29
   :linenos:
   
   def top_n_keywords_in_range(t,f,top = 100):
        """Analyse the plot (story abstract) of movies,
        then count the key words (get rid of stopsswords).
        
        :param year: The given year
        :type year: Integer
        :param top: The number speicifies rangking
        :type top: Integer
        :returns: A list of tuple (keyword,count)
        """
        result = []
        data = readDataInRange(t,f,False, False)
        wlist = []
        for d in data:
            plot = d[1][7]
            words = cleanDoc(plot)
            wlist.extend(words)
        freq = nltk.FreqDist(wlist)
        freq = sortDict(freq)
        for k in freq.keys()[:top+1]:
            if k.lower() == "unknown":
                continue
            result.append((k, freq[k]))
        if t == f:
            fn = "top_{n}_{some}_{f}".format(n=top, some= "keywords", f=f)
        else:
            fn = "top_{n}_produktiv_{some}_{f}_{t}".format(n=top, some= "keywords", f=f,t=t)
        writeData(result, fn)
        
Results was like this:

    .. image:: _static/top_keywords.png
    
    
Production Analysis Process
--------------------------

Then the ranking of production.

    .. image:: _static/p.png
    
    
    
Absolute Data Analysis Process
-------------------------

This is a result of year 2003.

    * genres	24
    * max_rating	8.9
    * countries	78
    * runtime_min	8
    * runtime_sum	269348
    * languages	84
    * movies	3700
    * directors	3141
    * writers	4497
    * actors	10236
    * min_rating	1
    * runtime_average	95.4119730783
    * runtime_max	720
    * average_rating	5.9758499825


Awords Movies Analysis Process
------------------------

Best **Oscar** and **Golden Global** movies of a given year.

code:

.. code-block:: python
   :emphasize-lines: 12,26,29
   :linenos:
   
   def best_n_awarded_movies_in_range(f,t, award="o"):
        """Use the imdb rating to rank the movies, that won oscar award.
        
        :param f: from a year
        :type f: int
        :param t: to a year
        :type t: string
        :param award: The award : {o:oscar, g:golden_global
        :type award: String
        :returns: none
        """
        data = readDataInRange(f,t,True,False)
        award = award[0].lower()
        awards = {"o":"oscar","g":"golden globe"}
        result = []
        p = r"\d+.{a}".format(a=awards[award])
        p = reg.compile(p)
        for d in data:
            y = d[0]
            m = d[1]
            aw = m[14].lower()
            if reg.search(p,aw):
                r = reg.search(p,aw).group(0)
                r = r.split(" ")
                result.append((m[4], float(m[8]), int(r[0]),r[1],y, m[9],m[5],))
        result = sorted(result, key = lambda t : t[1], reverse = True)
        if t == f:
            fn = "best_{a}_movie_in_{f}".format(a=awards[award], f=f)
        else:
            fn = "best_{a}_rated_movie_in_{f}_{t}".format(a=awards[award], f=f,t=t) 
        writeData(result, fn)


Best rated movies Analysis Process
--------------------------

Output the top n best reted movies of a given year.

.. code-block:: python
   :emphasize-lines: 12,26,29
   :linenos:

    def best_n_rated_movie_in_range(f, t, top=100):
        """Use the imdb rating to compute the value of a director.
        
        :param f: from year
        :type f: Int
        :param t: to year
        :type t: Int
        :param top: A rank number
        :type top: Int
        :returns: A list of tuples (directorname, rating)
        """
        data = readDataInRange(f,t)
        data = [(x[1][1],float(x[1][2]),x[1][4]) for x in data if float(x[1][2]) > 0]
        dt = sorted(data, key = lambda t: t[1], reverse=True)[:top+1]
        if t == f:
            fn = "best_{n}_rated_movie_in_{f}".format(n=top, f=f)
        else:
            fn = "best_{n}_rated_movie_in_{f}_{t}".format(n=top, f=f,t=t)
        writeData(dt,fn)
