# Dec. 08, Challenge 1

# initialise vars to use
register_db = {}

def change_register(action, amount, register):
    if not (register in register_db):
        register_db[register] = 0
    if action == "inc":
        register_db[register] += amount
    elif action == "dec":
        register_db[register] -= amount

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

    if condition_operator == ">" and condition_register > condition_amount:
        change_register(action, amount, register)
    elif condition_operator == ">=" and condition_register >= condition_amount:
        change_register(action, amount, register)
    elif condition_operator == "<" and condition_register < condition_amount:
        change_register(action, amount, register)
    elif condition_operator == "<=" and condition_register <= condition_amount:
        change_register(action, amount, register)
    elif condition_operator == "!=" and condition_register != condition_amount:
        change_register(action, amount, register)
    elif condition_operator == "==" and condition_register == condition_amount:
        change_register(action, amount, register)

print(max(register_db.iterkeys(), key=(lambda key: register_db[register])))
