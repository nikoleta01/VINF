# naive way of searching, line by line, without the use of indexing
# newFile = open("shortenedFileDic.txt", "r", encoding="utf8")
# for line in newFile:
#     if "Jack Bauer" in line:
#         print(line)

from whoosh import index
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.index import open_dir
import sys

ix = open_dir("index")
word = input("Enter wikipedia article name: ") 

from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser("english", ix.schema).parse(f"{word} OR (spanish:{word}) OR (french:{word})")
    results = searcher.search(query)
    length = sys.getsizeof(results)
    print(results[0:length])