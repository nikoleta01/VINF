# VINF
V súbore preprocessing.py sa vykonáva predspracovanie dát na pôvodnom súbore interlanguage_links_en.ttl z DBPedie. Výsledkom spustenia tohto súboru je vytvorenie súboru shortenedFile.txt.

V súbore indexing.py dochádza k indexovaniu. Výsledkom spustenia tohto súboru je vytvorenie zložky index, ak ešte neexistuje. Predpokladom na spustenie je prítomnosť súboru shortenedFile.txt, na ktorom sa index vytvára.

Návod na spustenie:
1. Ak máme stiahnutý súbor shortenedFile.txt, mali by sme spustiť súbor pre indexovanie - indexing.py, kde sa následne vytvorí zložka index.
2. Keď už máme vytvorenú zložku index, môžeme spúšťať hlavný program, ktorý je v search.py, kde sa vykonáva hľadanie názvov článkov. 
3. Spustíme search.py, od používateľa je vypýtaný používateľský vstup, kde zadá názov článku, ktorý chce vyhľadať v rôznych jazykových verziách a program mu vráti najlepšie výsledky.
