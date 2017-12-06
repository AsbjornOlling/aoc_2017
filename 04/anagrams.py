# December 04, challenge 2
# GOLD STAR GOT
# Answer: 251

import csv

# checks for anagrams in phrase
# two words are anagrams, if they
# have the same amount of every char
def is_valid(passphrase):
    word_id_list = []
    
    # build word_id dict
    for word in passphrase:
        word_id = {}
        for char in word:
            if char in word_id.keys():
                word_id[char] += 1
            else:
                word_id[char] = 1
        
        # check list then add
        if word_id in word_id_list:
            return False
        word_id_list.append(word_id)

    # return true if no anagrams found
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
