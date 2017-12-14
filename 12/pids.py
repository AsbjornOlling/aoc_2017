# December 12, challenge 1

connected_to_0 = ["0"]

# read file
input_file = open("input.txt")

# loop until pass with no changes
changed = True
passno = 0
while changed:
    changed = False
    passno += 1

    # go through lines in input
    for input_line in input_file:

        # parse text into ordered array
        line = input_line.strip("\n").replace(" <-> "," ").replace(", "," ").split(" ")

        # check if program connected to 0
        main_program = line[0]
        if main_program in connected_to_0:

            print(main_program + " connects "+ str(line[1:]))

            # if main is connected to 0, all its connections are too
            for i in range(1, len(line)):
                if not (line[i] in connected_to_0): # only add if not already there
                    changed = True
                    connected_to_0.append(line[i])

print("")
print("Passes done: "+str(passno))
# no of elements connected to 0
print("Size of group: "+str(len(connected_to_0)))
