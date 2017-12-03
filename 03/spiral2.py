import sys

# Dec 03, challenge 02
# A way better + faster solution
# written from scratch when starting challenge 2

# Note:
# the optimal solution would be to use pre-generated integer sequences
# e.g. counting the odd squares in the bottom-left corner
# but hey - that wasn't as fun

max_num = 32
dir_list = ['E', 'N', 'W', 'S'] # rotate through this ccw
dir_index = 0
dir_current = dir_list[dir_index]

# grid parameters
grid_size = 1000  # arbitrary large number that works
origin_coord = (grid_size//2, grid_size//2)  # start in the middle
coord = origin_coord

# build  grid
grid = []
for i in range(0, grid_size):
    grid.append([None] * grid_size)


# prints the spiral to stdout
#def printSpiral():
#    for row in grid:
#        for number in row:
#            if number != None:
#                sys.stdout.write(number)
#
#   sys.stdout.write("\r\n")


# do the first element manually
grid[coord[0]][coord[1]] = 1

run_length = 1
element = 2 # starting with the 2nd element

while element < 10:
    # run twice before incrementing runlength
    for n in range(0, 2):

        # do a run of run_length
        for i in range(0, run_length):
            # increment coord
            if dir_current == 'E':
                #print("moving right")
                coord = (coord[0]+1, coord[1])
            elif dir_current == 'N':
                #print("moving up")
                coord = (coord[0], coord[1]-1)
            elif dir_current == 'W':
                #print("moving left")
                coord = (coord[0]-1, coord[1])
            elif dir_current == 'S':
                #print("moving down")
                coord = (coord[0], coord[1]+1)

            print("element: "+str(element))
            # find value of num
            neighbor_sum = 0
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    if (j, k) != (0, 0) and grid[coord[0]+j][coord[1]+k] != None:
#                        print("adding: " + str(grid[coord[0]+j][coord[1]+k]) + " from coord: "+ str((coord[0]+j, coord[1]+k)))

                        neighbor_sum += grid[coord[0] + j][coord[1] + k]

            print(neighbor_sum)
            # then add number on the new coord
            grid[coord[0]][coord[1]] = neighbor_sum
            
            #count number placed
            element += 1

        # rotate to do another stretch
        dir_index += 1
        dir_current = dir_list[dir_index % len(dir_list)]

    # increment length every second run
    run_length += 1

#printSpiral() 


