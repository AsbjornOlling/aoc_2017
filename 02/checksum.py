# Dec 02, Challenge 1
# Compute checksum of a tab-separated list of ints
# checksum is the sum of the difference between largest and smallest elements in a single row

# GOLD STAR WON

import csv

with open("spreadsheet.txt") as sheet:
    diffsum = 0
    for line in csv.reader(sheet, delimiter="\t"):
        line.sort(key=int) # convert from string to int and sort
        #print(line)
        diff = int(line[len(line)-1]) - int(line[0])
        diffsum += diff

print(diffsum)
            
