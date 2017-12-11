# Dec 09, challenge 1
# GOLD STAR GOT

# load input file
# main input file is only one line
for line in open("input.txt"):

    # start vars
    group_level = 0
    points = 0

    # first go through and handle escape chars
    i = 0
    while i < len(line):
        # remove chars after !
        if line[i] == "!":
            line = line[:i] + " " + line[i+2:]
        i += 1

    # then do the rest
    i = 0
    while i < len(line):
        # get points
        if line[i] == "{":
            group_level += 1
            points += group_level

        # decrease points value
        elif line[i] == "}" and group_level > 0:
            group_level -= 1

        # move forward until garbage block closes
        elif line[i] == "<":
            while line[i] != ">":
                i += 1

        # move on to next line[i]
        i += 1

    print(str(points))
