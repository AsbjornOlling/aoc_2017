# December 04, challenge 2
import csv

# checks for repeated words
def is_valid(passphrase):
    
    for word in passphrase:

        # check for repetitions
        if word in words_checked:
            return False

        # add word to list
        words_checked.append(word)

    # if no repetitions found
    return True


# counter var
valid_passphrases = 0

# open file of passphrases
with open("passwords.txt") as passwords_file:
    for passphrase in csv.reader(passwords_file, delimiter=" "):

        # count as valid password, if no repetitions found
        if is_valid(passphrase):
            valid_passphrases += 1

print(valid_passphrases)
