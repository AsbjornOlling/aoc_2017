# December 06, challenge 1 + 2
# GOLD STARS GOT

import csv

banks_list = []
states_list = []

# put banks into list
with open("banks.txt") as banks_file:
    for line in csv.reader(banks_file, delimiter="\t"):
        for bank in line:
            banks_list.append(int(bank))

cycles_count = 0
while not banks_list in states_list:
    # add current state to list of previous states
    states_list.append(banks_list[:])
    cycles_count += 1

    # get index of biggest bank
    i = banks_list.index(max(banks_list))

    # take all the memory in that bank
    hand = banks_list[i]
    banks_list[i] = 0

    # start redistributing
    while hand > 0:
        i = (i+1) % len(banks_list)
        banks_list[i] += 1
        hand -= 1

    # debug bit
    #print("CURRENT STATE:" + str(banks_list))
    #print("LIST OF STATES:")
    #print(str(states_list))

print(cycles_count)
loop_cycle_size = len(states_list) - states_list.index(banks_list)
print(loop_cycle_size)
