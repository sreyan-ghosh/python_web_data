import urllib.request, urllib.parse, urllib.error # a library that concises the function of the socket library

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # this is a filehandler

counts = {}
for line in file:
    w = line.decode().strip()
    words = line.decode().split() # decoding because we are receiving byte format data. decoding to utf-8
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(w)
print(counts) # returns a word count dictionary.