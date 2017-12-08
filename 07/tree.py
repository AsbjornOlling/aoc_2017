# December 07, challenge 1
# find the bottom program

class Program:
    def __init__(self, line):
        # remove newline char
        line = line[:len(line)-1]
        # then parse line
        self.name = line[:4]
        self.weight = line[6:8]
        children_string = line[13:]
        # then make list of children
        self.children_list = [] # avoid error when pulling list
        if len(children_string) > 0:
            self.children_list = children_string.split(", ")


# read file, generate Program objects
list_of_programs = []
with open ("test.txt") as input_file:
    for line in input_file:
        list_of_programs.append(Program(line))

# if a program is nobody's child, it's the bottom
# so make complete list of children to check against
all_children = []
for program in list_of_programs:
    for child in program.children_list:
        all_children.append(child)

# then look for programs who's nobodys child:
for program in list_of_programs:
    if not (program.name in all_children):
        print(program.name)
