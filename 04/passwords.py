# December 04, challenge 1
# GOLD STAR GOT
# Answer: 466

import csv

valid_passphrases = 0

# open file of passphrases
with open("passwords.txt") as passwords_file:
    for passphrase in csv.reader(passwords_file, delimiter=" "):

        # start looping through single passphrase
        words_checked = []
        passphrase_repeats = False
        for word in passphrase:

            # check for repetition
            if word in words_checked:
                passphrase_repeats = True

            # add word to list
            words_checked.append(word)

        # count as valid password, if no repetitions found
        if not passphrase_repeats:
            valid_passphrases += 1

print(valid_passphrases)
