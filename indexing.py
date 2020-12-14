from whoosh import index
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
import os.path
from whoosh.index import open_dir

englishPrefix = 'en:'
frenchPrefix = 'fr:'
spanishPrefix = 'es:'

path = u"shortenedFile.txt"
# on windows systems there has to be an encoding specified, on Linux this can be omitted
file = open(path, "r", encoding="utf8")
schema = Schema(english=TEXT(stored=True), spanish=TEXT(stored=True), french=TEXT(stored=True))

if not os.path.exists("index"):
    os.mkdir("index")

ix = create_in("index", schema)
ix = open_dir("index")
writer = ix.writer()

for line in file:
    line = line.split(';')
    indexEs = [i for i, s in enumerate(line) if spanishPrefix in s]
    indexEn = [i for i, s in enumerate(line) if englishPrefix in s]
    indexFr = [i for i, s in enumerate(line) if frenchPrefix in s]
    if indexEn:
        english = line[indexEn[0]].split(':')
        english = english[1]
    if indexEs:
        spanish = line[indexEs[0]].split(':')
        spanish = spanish[1]
    else:
        spanish = ''
    if indexFr:
        french = line[indexFr[0]].split(':')
        french = french[1]
    else:
        french = ''
    writer.add_document(english=english, spanish=spanish, french=french)

writer.commit()