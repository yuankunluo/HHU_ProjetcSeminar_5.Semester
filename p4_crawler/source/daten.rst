Downloaded Daten Erklaerung 
=====================================

Ausgangsdaten bezogen von IMDB:
_______________________________

    .. image:: _static/csv_1.png


    Nachdem die Daten heruntergeladen wurden, liegen sie nun als CSV-Datei vor. Zu jedem untersuchten Jahr existiert eine eigene CSV-Datei. Die jeweiligen Datensätze umfassen eine laufende ID, die von der IMDB-Datenbank angehängt wurde. In der zweiten Spalte findet man den Titel des jeweiligen Films. Anschließend folgt in den nächsten Spalten das Erscheinungsdatum des Films und dessen Laufzeit.
    In der fünften Spalte ist der Regisseur vermerkt, der den Film gedreht hat. Als nächstes findet man in der sechsten Spalte die Namen der wichtigsten Schauspieler des Films. Als nächstes ist noch schlagwortartig das Genre des Films vermerkt, unter dem man ihn in der Datenbank finden kann. Um in der CSV-Datei eine Unterscheidung zu der normalen Kommaseparierung zu haben wurden sowohl die Namen der Schauspieler, als auch die verschiedenen Genres mit einem Semikolon unterteilt.
    In der achten Spalte findet sich zum Schluss noch eine kurze Beschreibung des Films.
    Nachdem die Daten heruntergeladen wurden, liegen sie nun als CSV-Datei vor. Zu jedem untersuchten Jahr existiert eine eigene CSV-Datei. Die jeweiligen Datensätze umfassen eine laufende ID, die von der IMDB-Datenbank angehängt wurde. In der zweiten Spalte findet man den Titel des jeweiligen Films. Anschließend folgt in den nächsten Spalten das Erscheinungsdatum des Films und dessen Laufzeit.
    In der fünften Spalte ist der Regisseur vermerkt, der den Film gedreht hat. Als nächstes findet man in der sechsten Spalte die Namen der wichtigsten Schauspieler des Films. Als nächstes ist noch schlagwortartig das Genre des Films vermerkt, unter dem man ihn in der Datenbank finden kann. Um in der CSV-Datei eine Unterscheidung zu der normalen Kommaseparierung zu haben wurden sowohl die Namen der Schauspieler, als auch die verschiedenen Genres mit einem Semikolon unterteilt.
    In der achten Spalte findet sich zum Schluss noch eine kurze Beschreibung des Films.


DaTail-Relation:
________________

    .. image:: _static/csv_2.png


    In dem Unterordner des von IMDB bezogenen Datensatzes findet sich die DaTail-Relation. 
    Im ersten Attribut(Spalte) ist der Plot des Films vermerkt, also kurz angerissen, worin es in dem Film geht. Als nächstes wurde in der Relation die empfohlene Altersfreigabe vermerkt nach amerikanischem Standart. 

    Diese umfasst folgende Altersstufen:
         *    (G)        für alle Altersstufen geeignet und freigegeben
         *    (PG)    Begleitung eines Erwachsenen wird empfohlen
         *    (PG-13)    Verschäfte Warnung nach PG
         *    (R)        unter 17 Jahren nur in Begleitung eines Erwachsenen
         *    (NC-17)    ab 18 Jahren. Die frühere Bezeichnung hierfür war (X)

     Im vierten Attribut findet sich die Angabe über die Orginalsprache des Films. Danach kommt noch einmal der Titel des Films, der sich hinter der zu anfangs genannten IMDB-ID befindet. Nun wird in der nächsten Spalte das Land genannt, in dem der Film gedreht wurde. Wenn der Drehort an verschiedenen Stellen auf der Welt lag, dann ist eine Mehrfachbesetzung zulässig. Im siebten Feld sind dann die wichtigsten Verantwortlichen für die Story genannt. Zum einen sind das die Drehbuchautoren, sofern mehrere mitgewirkt haben und es wird auch der Autor des Orginaltextes genannt, sofern es auf einem Buch basiert.
     Nun folgen Daten, die von IMDB selbst stammen. Hierzu zählt ein eigenes Ranking und das Datum, zu welchem Zeitpunkt das Ranking erstellt wurde. In der zehnten Spalte wird dann nochmal der Regisseur genannt.
     Weiterhin stehen einige Angaben in dieser Relation, die bereits in der Hauptrelation zu finden sind, als da wären das Veröffentlichungsdatum, die wichtigsten Schauspieler, das zugehörige Jahr und das Genre.
     In der 14. Spalte dann werden die Awards thematisiert. Hier lässt sich herausfinden, wie oft ein Film nominiert wurde und wie oft davon auch eine Auszeichnung verliehen worden ist.
     Zum Schluss findet sich nochmal die Laufzeit und ein Attribut, dass eine URL zu dem Filmplakat liefert.
=======
    In dem Unterordner des von IMDB bezogenen Datensatzes findet sich die DaTail-Relation. 
    Im ersten Attribut(Spalte) ist der Plot des Films vermerkt, also kurz angerissen, worin es in dem Film geht. Als nächstes wurde in der Relation die empfohlene Altersfreigabe vermerkt nach amerikanischem Standart. 

    Diese umfasst folgende Altersstufen:
         *    (G)        für alle Altersstufen geeignet und freigegeben
         *    (PG)    Begleitung eines Erwachsenen wird empfohlen
         *    (PG-13)    Verschäfte Warnung nach PG
         *    (R)        unter 17 Jahren nur in Begleitung eines Erwachsenen
         *    (NC-17)    ab 18 Jahren. Die frühere Bezeichnung hierfür war (X)

     Im vierten Attribut findet sich die Angabe über die Orginalsprache des Films. Danach kommt noch einmal der Titel des Films, der sich hinter der zu anfangs genannten IMDB-ID befindet. Nun wird in der nächsten Spalte das Land genannt, in dem der Film gedreht wurde. Wenn der Drehort an verschiedenen Stellen auf der Welt lag, dann ist eine Mehrfachbesetzung zulässig. Im siebten Feld sind dann die wichtigsten Verantwortlichen für die Story genannt. Zum einen sind das die Drehbuchautoren, sofern mehrere mitgewirkt haben und es wird auch der Autor des Orginaltextes genannt, sofern es auf einem Buch basiert.
     Nun folgen Daten, die von IMDB selbst stammen. Hierzu zählt ein eigenes Ranking und das Datum, zu welchem Zeitpunkt das Ranking erstellt wurde. In der zehnten Spalte wird dann nochmal der Regisseur genannt.
     Weiterhin stehen einige Angaben in dieser Relation, die bereits in der Hauptrelation zu finden sind, als da wären das Veröffentlichungsdatum, die wichtigsten Schauspieler, das zugehörige Jahr und das Genre.
     In der 14. Spalte dann werden die Awards thematisiert. Hier lässt sich herausfinden, wie oft ein Film nominiert wurde und wie oft davon auch eine Auszeichnung verliehen worden ist.
     Zum Schluss findet sich nochmal die Laufzeit und ein Attribut, dass eine URL zu dem Filmplakat liefert.

