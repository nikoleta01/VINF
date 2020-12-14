# VINF
V súbore preprocessing.py sa vykonáva predspracovanie dát na pôvodnom súbore interlanguage_links_en.ttl z DBPedie. Výsledkom spustenia tohto súboru je vytvorenie súboru shortenedFile.txt.

V súbore indexing.py dochádza k indexovaniu. Výsledkom spustenia tohto súboru je vytvorenie zložky index, ak ešte neexistuje. Predpokladom na spustenie je prítomnosť súboru shortenedFile.txt, na ktorom sa index vytvára. V tomto repozitári je vzorka týchto dát s 200 riadkami, pôvodný súbor je uložený na Google Disku - https://drive.google.com/drive/folders/1pk5kKSuzGSqP5mcW57Lh8JvZ3989aJn1?usp=sharing

V súbore statistics.py sa vykonávajú číselné štatistiky na súbore shortenedFile.txt, ktoré sú zhrnuté v dokumentácii v kapitole výsledkov na Google Disku - https://docs.google.com/document/d/1yDJgDgkJMmK91vx55miECs1SlhTRi6alGNQAhw9c89U/edit?usp=sharing

Návod na spustenie:
1. Ak máme stiahnutý súbor shortenedFile.txt, mali by sme spustiť súbor pre indexovanie - indexing.py, kde sa následne vytvorí zložka index.
2. Keď už máme vytvorenú zložku index, môžeme spúšťať hlavný program, ktorý je v search.py, kde sa vykonáva hľadanie názvov článkov. 
3. Spustíme search.py, od používateľa je vypýtaný používateľský vstup, kde zadá názov článku, ktorý chce vyhľadať v rôznych jazykových verziách a program mu vráti najlepšie výsledky.
