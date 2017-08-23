# A small python script that takes a list of words (strings) as 1 argument,
# and a text file as another argument, and checks if any words in
# the list are present in the text file. If so, it prints to stdout
# the word (string) that was found.
# 
# Author: Dakota Chambers
#         Center for High Throughput Computing
#         08 23 2017
#
# Usage: $ python check-file-for-words-from-list.py <word list> <text file>
#
#


import os
import sys

if len(sys.argv) > 3:
    print 'Too many command line arguments. Expected: 2 [word list] [text file].'
    sys.exit()
elif len(sys.argv) < 3:
    print 'Too few command line arguments. Expected: 2 [word list] [text file].'
    sys.exit()

wordList = open(sys.argv[1], 'r')
textFile = open(sys.argv[2], 'r')

wordListArray = []

for line in wordList:
    wordListArray.append(line.rstrip())

for line in textFile:
    for word in wordListArray:
        if word in line:
            print word
