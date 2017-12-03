# Dec 02, Challenge 2
# Find the only two evenly dividable numbers in each row
# find the sum of the result of the division in all the rows

# GOLD STAR GOT

import csv

with open("spreadsheet.txt") as sheet:
    divsum=0
    for line in csv.reader(sheet, delimiter="\t"):
        #line.sort(key=int) # convert from string to int and sort
        # convert to int
        line = list(map(int, line)) 
        for num in line:
            for other_num in line:
                if not num == other_num and num % other_num == 0:
                    #print("DIVISIBILITY FOUND")
                    #print(num, other_num)
                    divsum += int(num / other_num)

print(divsum)

