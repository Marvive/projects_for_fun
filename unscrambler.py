from itertools import permutations
import re

with open("/usr/share/dict/words") as f:
    data = f.readlines()


letters = list(input("Enter letters to unscramble:\n"))


def permutates(letters, number):
    return [''.join(i) for i in permutations(letters, number)]


combo_list_3 = permutates(letters, 3)
combo_list_4 = permutates(letters, 4)
combo_list_5 = permutates(letters, 5)
combo_list_6 = permutates(letters, 6)

valid_list_3 = []
valid_list_4 = []
valid_list_5 = []
valid_list_6 = []

counter = 0
for line in data:
    if line.strip() in combo_list_3:
        valid_list_3.append(line.strip())
    elif line.strip() in combo_list_4:
        valid_list_4.append(line.strip())
    elif line.strip() in combo_list_5:
        valid_list_5.append(line.strip())
    if line.strip() in combo_list_6:
        valid_list_6.append(line.strip())


print(f"""
Note This list excludes plurals!

Three Letter Words: 
{valid_list_3}

Four Letter Words: 
{valid_list_4}

Five Letter Words: 
{valid_list_5}

Six Letter Words: 
{valid_list_6}
""")
