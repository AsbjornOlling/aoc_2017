import sys

## GOLD STAR GOT
## (but this solution is terrible and very slow)
# answer: 475

class Number:
    def __init__(self, coord, number):
        self.coord = coord
        self.number = number

def listContainsCoord(coord):
    for num in num_list:
        if num.coord == coord:
            return True
    return False

max_num=277678 # stop after this number is placed
num_list = [] # list of Number objects
dir_list = ['E', 'N', 'W', 'S'] # rotate through this ccw
dir_index = 0
dir_current = dir_list[dir_index]

# these are incremented
coord = (0, 0)

# main counting loop
for number in range(1, max_num+1):
    num_list.append(Number(coord, number))
    print("PLACING:"+str(number))

    # find coord to check and get new coord
    if dir_current == 'E':
        # check up
        coord_to_check = (coord[0], coord[1]+1)
    elif dir_current == 'N':
        # check left
        coord_to_check = (coord[0]-1, coord[1])
    elif dir_current == 'W':
        # check down
        coord_to_check = (coord[0], coord[1]-1)
    elif dir_current == 'S':
        # check right
        coord_to_check = (coord[0]+1, coord[1])

    # rotate direction ccw if there's space
    if not listContainsCoord(coord_to_check):
       dir_index += 1
       dir_current = dir_list[dir_index % len(dir_list)]
    
    # increment coord
    if dir_current == 'E':
        coord = (coord[0]+1, coord[1])
    elif dir_current == 'N':
        coord = (coord[0], coord[1]+1)
    elif dir_current == 'W':
        coord = (coord[0]-1, coord[1])
    elif dir_current == 'S':
        coord = (coord[0], coord[1]-1)

# now print the spiral
# first sort the list by coords, x first
num_list.sort(key=lambda c: c.coord)
prev_x = -2
for num in num_list:
    # make linebrak if changing y coords
    if prev_x != num.coord[0]:
        sys.stdout.write("\r\n")

    sys.stdout.write(str(num.number)+ "\t")

    prev_x = num.coord[0]
sys.stdout.write("\r\n")

## print the last coord, and distance to (0,0)
print("Last coord:" + str(num_list[len(num_list)-1].coord))
distance = abs(num_list[len(num_list)-1].coord[0]) + abs(num_list[len(num_list)-1].coord[1])
print(distance)


