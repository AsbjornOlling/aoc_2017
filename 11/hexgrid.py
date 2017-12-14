# December 11, challenge 1

# infinite vertical hex grid
# hex grid built using axial coords
# neighbors: nw, n, ne, se, s, sw,

# if the hex is at coord 0,0 - these are its neighbors:
# nw =-1, 0
# n =  0,-1
# ne = 1,-1
# se = 1, 0
# s =  0, 1
# sw =-1, 1

class hex:
    def __init__(self, coords):
        self.x, self.y = coords

input_file = open("test.txt")

for line in input_file:
    # init axial grid coords
    x = 0
    y = 0

    # move using axial coords
    input_array = line.strip("\n").split(",")
    for direction in input_array:
        if direction == "nw":
            x -= 1
        elif direction == "n":
            y -= 1
        elif direction == "ne":
            x += 1
            y -= 1
        elif direction == "se":
            x += 1
        elif direction == "s":
            y += 1
        elif direction == "sw":
            x -= 1
            y += 1

    # find z coord from axial
    z = (x + y) * (-1)

    # calculate distance
    dist = (abs(x) + abs(y) + abs(z))/2

    print("Distance: " + str(dist))
