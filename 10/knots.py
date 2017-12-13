# December 10, challenge 2
# GOLD STAR GOT on challenge 1

## TODO

# read ascii in input file
# do 64 runs total (preserving cur_pos and skip_size)
# then bitwise xor blocks of 16 ( so you have 16 nums ) 

# init vars
cur_pos = 0
skip_size = 0
list_length = 256
num_list = []
for i in range(0, list_length):
    num_list.append(i)
suffix = [17, 31, 73, 47, 23]


# read input
input_file = open("test.txt")

# really, it's only one line
# so this is the main block of code
for line in input_file:

    # convert each char to an ascii code
    line = line.strip("\n")
    input_lengths = []
    for char in line:
        input_lengths.append(ord(char))
    for num in suffix:
        input_lengths.append(num)
    print(input_lengths)

    # main loop
    # extract and reverse substring
    for substring_length in input_lengths:
        # extract substring
        substring = []
        for i in range(0, substring_length):
            substring.append(num_list[(cur_pos + i) % list_length])

        # reverse substring
        substring = substring[::-1]
        #print(substring)

        # now place substring back on num_list
        for i in range(0, substring_length):
            num_list[(cur_pos + i) % list_length] = substring[i]

        #print(num_list)

        cur_pos += int(substring_length) + skip_size
        skip_size += 1

    print(num_list[0] * num_list[1])
