# December 07, challenge 1
# find the bottom program
# GOLD STAR GOT

class Program:
    def __init__(self, line):
        # remove newline char
        line = line[:len(line)-1]
        # parsing values
        words_list = line.split(" ")
        self.name= words_list[0]
        self.weight = int(words_list[1][1:len(words_list[1]) - 1])
        self.children = words_list[3:]
        for i in range(0, len(self.children)): # remove trailing commas
            if self.children[i][len(self.children[i])-1] == ",":
                self.children[i] = self.children[i][:len(self.children[i])-1]


    # make list containing child objects
    def find_children_objects(self):
        self.child_objects = []
        for child_string in self.children:
            for program in list_of_programs:
                if child_string == program.name:
                    self.child_objects.append(program)
                    program.parent = self


    def weigh_recursive(self):
        weight = self.weight
        for child in self.child_objects:
            weight += child.weigh_recursive()
        return weight


# this is the solution to challenge 1
def find_bottom_program():
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
                return program


def check_balance(plateholder_program):
    # start looking for the program with wrong weight
    #
    # get weight of the programs on bottom plate
    comparison_dict = {}
    for child in plateholder_program.child_objects:
        comparison_dict[child] = child.weigh_recursive()

    # start looking for the outlier
    # calculate average weight
    average = 0
    for program, weight in comparison_dict.items():
        average += weight
    average = average / len(comparison_dict)
    # find the program furthest from average weight
    largest_diff = 0
    outlier_program = None
    for program, weight in comparison_dict.items():
        if abs(weight-average) > largest_diff:
            largest_diff = abs(weight-average)
            outlier_program = program
    # ^outlier found

    # if it's unbalanced
    if outlier_program != None:
        # print stats for all programs on plate
        for program, weight in comparison_dict.items():
            print(program.name + " "+ str(weight))
        print("")

        # then recurse
        print("Checking the outlier: "+outlier_program.name)
        check_balance(outlier_program)

    # if it's balanced
    else:
        print(plateholder_program.name + "'s plate is balanced!")

        # check how much it's off, compared to neighbors
        print("Comparing with "+plateholder_program.name+"'s neighbors")
        for neighbor_program in plateholder_program.parent.child_objects:
            if neighbor_program.name != plateholder_program:
                diff = abs(neighbor_program.weight - plateholder_program.weight)
                print("Checking "+neighbor_program.name+" and "+plateholder_program.name)
                print("Weight diff found: "+str(diff))
                print("")


# read file, generate Program objects
list_of_programs = []
with open ("input.txt") as input_file:
    for line in input_file:
        list_of_programs.append(Program(line))

# then generate child lists containing objects
for program in list_of_programs:
    program.find_children_objects()

# then start looking for the off-balance program
check_balance(find_bottom_program())



# WHAT TODO
# check if balanced
# if not balanced, check the balance of the outlier
# do this until balance is found
# then figure smth out
