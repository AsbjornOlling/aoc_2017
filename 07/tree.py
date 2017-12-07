# December 07, challenge 1

import csv

list_of_programs = []


class Program:
    def __init__(self, line):
        self.name = line[:5]
        self.weight = line[6:8]
        children = line[13:]
        print(children)

with open ("test.txt") as input_file:
    for line in input_file:
        list_of_programs.append(Program(line))
