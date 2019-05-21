import string
import os

# directory of text files
directory = ""

#list of search terms
searchterms = ['', '']

def wordcount(filename, searchterms):
    try:
        dircount = 0
        file = open(os.path.join(directory, filename), 'r')
        read = file.readlines()
        file.close()
        results = []
        for word in searchterms:
            lower = word.lower()
            count = 0
            for line in read:
                l = line.split()
                for t in l:
                    t = t.lower()
                    t = ''.join(w for w in t if w not in string.punctuation)
                    if t == lower:
                        count += 1
            results.append((word, count))
        return(results)
    except FileExistsError:
        print('file not there')

for s in searchterms:
    dircount = 0
    for filename in os.listdir(directory):
        file_word_counts = wordcount(filename, searchterms)
        for (a,b) in file_word_counts:
            if s == a:
                dircount += b
    print (s, dircount)
