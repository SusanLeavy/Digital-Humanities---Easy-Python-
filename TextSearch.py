from flashtext import KeywordProcessor


directory = ""
searchterms = []
keyword_processor = KeywordProcessor()
dirtotal = []
for filename in os.listdir(directory):
    keyword_processor.add_keywords_from_list(searchterms)
    file = open(os.path.join(directory, filename), 'r')
    read = file.read()
    keywords_found = keyword_processor.extract_keywords(read, span_info=True)
    dirtotal = dirtotal+keywords_found

dictionary_freq = {}
for a, b, c in dirtotal:
    dictionary_freq[a] = dictionary_freq.get(a, 0) + 1
print(dictionary_freq)
