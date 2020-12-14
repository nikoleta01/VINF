# naive way of searching, line by line, without the use of indexing
newFile = open("shortenedFile.txt", "r", encoding="utf8")
# englishCount = 0
# spanishCount = 0
# frenchCount = 0

# for line in newFile:
#     if "en:" in line:
#         englishCount += 1
#     if "es:" in line:
#         spanishCount += 1
#     if "fr:" in line:
#         frenchCount += 1

# print(englishCount, spanishCount, frenchCount)

count = 0
for line in newFile:
    if "es:" in line and "en:" in line and "fr:" in line:
        splitted = line.split(";")
        splitted = splitted[0]
        splitted = splitted.split(":")
        word = splitted[1]
        # print(word)
        if f"fr:{word}" in line and f"es:{word}" in line:
            count += 1

print(count)

count = 0
for line in newFile:
    if "es:" in line and "en:" in line and "fr:" in line:
        splitted = line.split(";")
        splitted = splitted[0]
        splitted = splitted.split(":")
        word = splitted[1]
        # print(word)
        if f"fr:{word}" in line:
            count += 1

print(count)

count = 0
for line in newFile:
    if "es:" in line and "en:" in line and "fr:" in line:
        splitted = line.split(";")
        splitted = splitted[0]
        splitted = splitted.split(":")
        word = splitted[1]
        # print(word)
        if f"es:{word}" in line:
            count += 1

print(count)

# count = 0
# for line in newFile:
#     if "en:" in line and "fr:" in line and "es:" not in line:
#         count += 1
#         # print(line)

# print(count)

