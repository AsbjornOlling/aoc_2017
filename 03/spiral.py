import sys

# Dec 03, challenge 01
# A way better + faster solution
# written from scratch when starting challenge 2

# Note:
# the optimal solution would be to use pre-generated integer sequences
# e.g. counting the odd squares in the bottom-left corner
# but hey - that wasn't as fun

max_num = 277678
num_list = []
dir_list = ['E', 'N', 'W', 'S'] # rotate through this ccw
dir_index = 0
dir_current = dir_list[dir_index]
coord = (0, 0)

class Number:
    def __init__(self, coord, number):
        self.coord = coord
        self.number = number


# prints the spiral to stdout
def printSpiral():
    # first sort the list by coords, y first
    num_list.sort(key=lambda c: (c.coord[1], c.coord[0]))

    prev_y = num_list[0].coord[1]
    for num in num_list:
        if prev_y != num.coord[1]:
            sys.stdout.write("\r\n")

        sys.stdout.write(str(num.number)+ "\t")

        prev_y = num.coord[1]
    sys.stdout.write("\r\n")


# do the first num manually
num = 1
num_list.append(Number(coord, num))
run_length = 1
while num <= max_num:
    # run twice before incrementing runlength
    for n in range(0, 2):
        for i in range(0, run_length):
            # increment num
            num += 1
            # increment coord
            if dir_current == 'E':
                coord = (coord[0]+1, coord[1])
            elif dir_current == 'N':
                coord = (coord[0], coord[1]-1)
            elif dir_current == 'W':
                coord = (coord[0]-1, coord[1])
            elif dir_current == 'S':
                coord = (coord[0], coord[1]+1)
            # then add number to the new coord
            num_list.append(Number(coord, num))
            if num == max_num:
                print(abs(coord[0]) + abs(coord[1]))
        # rotate, before doing another run with same length
        dir_index += 1
        dir_current = dir_list[dir_index % len(dir_list)]
    run_length += 1

#printSpiral() 


