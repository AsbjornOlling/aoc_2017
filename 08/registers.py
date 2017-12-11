# Dec. 08, Challenge 1

# initialise vars to use
register_db = {}
line_no = 0


# read input file
for line in open("input.txt"):
    line_array = line.strip("\n").split(" ")

    line_no += 1

    # parse one line
    register = line_array[0]
    action = line_array[1]
    amount = int(line_array[2])
    condition_register = line_array[4]
    condition_operator = line_array[5]
    condition_amount = line_array[6]

    # check if condition met
    if (
           (condition_operator == ">" 
            and condition_register > condition_amount)
        or (condition_operator == "<" 
            and condition_register < condition_amount)
        or (condition_operator == ">=" 
            and condition_register >= condition_amount)
        or (condition_operator == "<=" 
            and condition_register <= condition_amount)
        or (condition_operator == "!=" 
            and condition_register != condition_amount)
        or (condition_operator == "==" 
            and condition_register == condition_amount)
    ):
        print(line+" on "+line_no+" met!")
	# increment or decrement if met
	if not (register in register_db):
	    register_db[register] = 0
	if action == "inc":
	    register_db[register] += amount
            print("Incrementing "+register)
	elif action == "dec":
	    register_db[register] -= amount
            print("Decemenenting "+register)

# find highest value (answer to challenge 1)
highest_value = 0
for key, value in register_db.items():
    if value > highest_value:
        highest_value = value
print(str(highest_value))
