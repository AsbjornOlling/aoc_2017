# Dec. 08, Challenge 1 and 2
# GOLD STARS GOT

# initialise vars to use
register_db = {}
line_no = 0
highest_value_ever = 0

# read input file
for line in open("input.txt"):
    line_no += 1

    # parse one line
    line_array = line.strip("\n").split(" ")
    register = line_array[0]
    action = line_array[1]
    amount = int(line_array[2])
    condition_register = line_array[4]
    condition_operator = line_array[5]
    condition_amount = int(line_array[6])

    # put registers in dictory if new
    if not (register in register_db):
        register_db[register] = 0
    if not (condition_register in register_db):
        register_db[condition_register] = 0

    # check if condition met
    if ((condition_operator == ">" and register_db[condition_register] > condition_amount)
    or (condition_operator == "<" and register_db[condition_register] < condition_amount)
    or (condition_operator == ">=" and register_db[condition_register] >= condition_amount)
    or (condition_operator == "<=" and register_db[condition_register] <= condition_amount)
    or (condition_operator == "!=" and register_db[condition_register] != condition_amount)
    or (condition_operator == "==" and register_db[condition_register] == condition_amount)):
        # debuggin lines
        print(condition_register + " is " + str(register_db[condition_register]))
        print(condition_register + " is " + condition_operator +" "+ str(condition_amount))

	# increment or decrement if met
	if action == "inc":
	    register_db[register] += amount
            # is this the highest value ever? (challenge 2)
            if register_db[register] > highest_value_ever:
                highest_value_ever = register_db[register]

	elif action == "dec":
	    register_db[register] -= amount
else:
    # debuggin lines
        print(condition_register + " is " + str(register_db[condition_register]))
        print(condition_register + " is not " + condition_operator +" "+ str(condition_amount))

# find highest value (answer to challenge 1)
highest_value = 0
for key, value in register_db.items():
    if value > highest_value:
        highest_value = value

print(str(highest_value))
print(str(highest_value_ever))
