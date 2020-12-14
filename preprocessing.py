import re
shortenedFile = open("shortenedFile.txt", "a", encoding="utf8")
spanishPattern = '.es'r'\..'
frenchPattern = '.fr'r'\..'
englishPattern = './/dbped.'
qEntityPattern = '/entity/Q.'
englishPrefix = 'en:'
frenchPrefix = 'fr:'
spanishPrefix = 'es:'

interlanguageLinks = open("interlanguage_links_en.ttl", "r", encoding="utf8")
check = 0
for line in interlanguageLinks:
    splittedLine = line.split(' ')
    splittedLine =  splittedLine[2]
    spanish = re.search(spanishPattern, splittedLine)
    french = re.search(frenchPattern, splittedLine)
    english = re.search(englishPattern, splittedLine)
    if(re.search(qEntityPattern, splittedLine) and check is 0):
        check += 1 
    elif(re.search(qEntityPattern, splittedLine) and check is not 0):
        shortenedFile.write('\n')
    if spanish or french or english:
        if spanish:
            prefix = spanishPrefix
        elif english:
            prefix = englishPrefix
        elif french:
            prefix = frenchPrefix
        splittedLine = splittedLine.split("/")
        articleName = splittedLine[4]
        temp = articleName.split(">")
        name = temp[0]
        name = name.replace("_", " ")
        shortenedFile.write(prefix + " " + name + "; ")    
    
interlanguageLinks.close()
shortenedFile.close()