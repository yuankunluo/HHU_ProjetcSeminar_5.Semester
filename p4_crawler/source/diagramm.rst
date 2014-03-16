Diagrammer Maker
======================================

Grafiken bezogen auf IMDB Results :
_______________________________

	Nachdem die Daten heruntergeladen wurden, wird das Script diagrammer.py gestartet um die Barplots zu erstellen.
	* Start mit python diagrammer.py
	Aus dem dataanylser.py wird das Modul für CSV Lesezugriffe verwendet. Um sich eine Dateiliste zu generieren, wird das Modul walk  aus os importiert und der Results Ordner, der Dateien für die Ausgabefunktion enthält, durchsucht. Damit werden alle Dateinamen in eine Liste gespeichert.
	Die Methode barplot wird so mehrmals von der Methode crashplot iterativ aufgerufen, je nachedem, wieviel csv Dateien im Results Ordner vorhanden sind.
	


Methode bar plot Beschreibung:
-----------------------------


	Zuerst wird die csv Datei eingelesen.
	Mit sorted wird nach dem zweiten Element in der Relation aufsteigend sortiert.Dazu wird die Methode sorted verwendet. Die Lambda Funktion weist den Filterschlüssel an die Sortierfunktion zu. Reverse option ist für das absteigende und aufsteigende Sortieren zuständig, die über den Boolean Wert eingestellt wird.
	Die Liste daraus wird auf die ersten 10 Werte zugeschnitten das geschieht Tupelweise, die Unterliste wird jeweils nochmal auf die ersten 2 Spalten Einträge zurechtgestützt.	
	Dann werden die Schlüssel und Werte mit einer List Comprehension aus utf-8 decodiert und in Variablen als separate Listen gespeichert.
    Die Werte werden für die Plottingfunktion aus matplotlib.pyplot  nach integer mit int() umgewandelt. Das geschieht auch über eine List Comprehension.  
    Mit plt.lim werden die Grenzen der Anzeige der Grafik eingestellt.
	Mit plt.bar werden die Balken aus den Werten gerendert und mit center zentriert.
	Die Beschreibungen, die unter der Grafik stehen werden  mit plt.ticks Funktion um 50 Grad gedreht und auf eine kleine Größe eingestellt, weil es oft mehrere Werte gibt.
    Mit str.replace werden aus dem Dateinamen unnötige Zeichenketten entfernt. Dannach wird die Grafik als png Datei im Diagram Ordner gespeichert.
	plt.close ist dafür, damit die Grafiken sich nicht gegenseitig überschreiben und jeweils eine separate Instanz wenn nötig gestartet wird.
	
	Probleme gab es mit den Überschriften, die seltsamerweise nicht angezeigt wurden.

Code
-------------------------------

.. code-block:: python
   :linenos:
   
   
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
