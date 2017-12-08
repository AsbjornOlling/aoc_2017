# December 07, challenge 1
# find the bottom program

class Program:
    def __init__(self, line):
        # remove newline char
        line = line[:len(line)-1]
        
        # better parsing
        words_list = line.split(" ")
        self.name= words_list[0]
        self.weight = int(words_list[1][1:len(words_list[1]) - 1])
        self.children = words_list[3:]
        for i in range(0, len(self.children)): # remove trailing commas
            if self.children[i][len(self.children[i])-1] == ",":
                self.children[i] = self.children[i][:len(self.children[i])-1]


    def debug(self):
        print("Name: "+self.name)
        print("Name length: "+str(len(self.name)))
        print("No. of children: "+str(len(self.children)))
        print("Children: "+str(self.children))
        print("Weight: "+str(self.weight))
        print("")


# read file, generate Program objects
list_of_programs = []
with open ("test.txt") as input_file:
    for line in input_file:
        list_of_programs.append(Program(line))

# if a program is nobody's child, it's the bottom
# so make complete list of children to check against
all_children = []
for program in list_of_programs:
    for child in program.children:
        all_children.append(child)

# then look for programs who's nobodys child:
for program in list_of_programs:
    # only check programs that have children
    if len(program.children):
        if not (program.name in all_children):
            #program.debug()
            print(program.name)
