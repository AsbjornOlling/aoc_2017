# December 06, challenge 1

import csv

banks_list = []

# put banks into list
with open("test.txt") as banks_file:
    for line in csv.reader(banks_file, delimiter="\t"):
        for bank in line:
            banks_list.append(bank)


for i in banks_list:
    print(i)
    print("blank")


