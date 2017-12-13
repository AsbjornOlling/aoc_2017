# December 10, challenge 1
# GOLD STAR GOT

# init vars
cur_pos = 0
skip_size = 0
list_length = 256
num_list = []
for i in range(0, list_length):
    num_list.append(i)


# read input
input_file = open("input.txt")

# really, it's only one line
# so this is the main block of code
for line in input_file:

    # read lengths into list
    input_lengths = line.strip("\n").split(",")

    # main loop
    # extract and reverse substring
    for substring_length in input_lengths:
        # extract substring
        substring = []
        for i in range(0, int(substring_length)):
            substring.append(num_list[(cur_pos + i) % list_length])

        # reverse substring
        substring = substring[::-1]
        #print(substring)

        # now place substring back on num_list
        for i in range(0, int(substring_length)):
            num_list[(cur_pos + i) % list_length] = substring[i]

        #print(num_list)

        cur_pos += int(substring_length) + skip_size
        skip_size += 1

    print(num_list[0] * num_list[1])
