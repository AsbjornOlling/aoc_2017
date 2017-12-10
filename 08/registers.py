# Dec. 08, Challenge 1

# initialise vars to use
register_db = {}

# read input file
for line in open("test.txt"):
    line_array = line.strip("\n").split(" ")

    # parse one line
    register = line_array[0]
    action = line_array[1]
    amount = int(line_array[2])
    condition_register = line_array[4]
    condition_operator = line_array[5]
    condition_amount = line_array[6]

    # test
    print("register: "+register)
    print("action: "+action)
    print("amount: "+str(amount))
    print("condition_register: "+str(condition_register))
    print("condition_operator: "+str(condition_operator))
    print("condition_amount: "+str(condition_amount))

