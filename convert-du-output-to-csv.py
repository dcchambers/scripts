# Reads in the output from $ du -csh --time * >> output.log
# and prints it to a CSV file in the format "date,user,sizeOfHomeDir"
#
# Usage: Run $ python convert-to-csv.py [arg1] [arg2]
# where [arg1] is the output.log file to be converted to CSV.
# and [arg2] is the name of the output CSV file.
#

import os
import sys

if len(sys.argv) > 3:
    print 'Too many command line arguments. Expected: 2 [input file] [output file].'
    sys.exit()
elif len(sys.argv) < 3:
    print 'Too few command line arguments. Expected: 2 [input file] [output file].'
    sys.exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

f2 = open(outputFile,'w+')
f2.write('date,user,size-of-homedir\n')

with open(inputFile,'r') as f1:
    for line in f1:
        tempArray = []
        tempArray = line.split('\t')
        # print tempArray #DEBUG
        f2.write(tempArray[1]+','+tempArray[2].rstrip('\n')+','+tempArray[0]+'\n')
