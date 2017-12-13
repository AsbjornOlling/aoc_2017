# December 10, challenge 2
# GOLD STAR GOT on challenge 1

## TODO

# then bitwise xor blocks of 16 ( so you have 16 nums ) 

# init vars
list_length = 256
suffix = [17, 31, 73, 47, 23]

# read input
input_file = open("test.txt")

# really, it's only one line in the real input
# but is useful for testing
# so this is the main block of code
for line in input_file:

    # reset counters for the hash
    cur_pos = 0
    skip_size = 0
    num_list = []
    for i in range(0, list_length):
        num_list.append(i)


    # convert each char to an ascii code
    line = line.strip("\n")
    input_lengths = []
    for char in line:
        input_lengths.append(ord(char))
    for num in suffix:
        input_lengths.append(num)

    # do 64 rounds, preserving skipsize and position
    for round_no in range(0, 64):
        # loop to extract, reverse, and reinset
        for substring_length in input_lengths:
            # extract substring
            substring = []
            for i in range(0, substring_length):
                substring.append(num_list[(cur_pos + i) % list_length])

            # reverse substring
            substring = substring[::-1]

            # now place substring back on num_list
            for i in range(0, substring_length):
                num_list[(cur_pos + i) % list_length] = substring[i]

            # change position on list
            cur_pos += int(substring_length) + skip_size
            skip_size += 1

    # when all rounds done
    # xor 16 blocks of 16 nums
    dense_hash_string = ""
    for i in range(0, 16):
        start_block = i*16
        end_block = start_block + 16
        block = num_list[start_block:end_block]
        xor = block[0] ^ block[1]
        for j in range(2, 16):
            xor ^= block[j]

        # make hexadecimal string, pad with 0
        dense_hash_substring = str(hex(xor))[2:]
        while len(dense_hash_substring) < 2:
            dense_hash_substring = "0" + dense_hash_string
        dense_hash_string += dense_hash_substring

    print(dense_hash_string)
