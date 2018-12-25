"""
Day 5
"""

# Part 1
def read_input(x):
    return open(x).read()

def react_polymers(x):
    change = 1
    while change > 0:
        x = list(x)
        original = len(x)
        for i in range(0, len(x) - 1):
            a = x[i]
            b = x[i + 1]
            if a.swapcase() == b:
                x[i] = x[i].replace(x[i], "")
                x[i + 1] = x[i + 1].replace(x[i + 1], "")
        x = "".join(x for x in x)
        after = len(x)
        change = original - after
    return x

x = read_input("data/5-1.txt")
x = react_polymers(x)

"The answer is: {}".format(len(x))

# Part 2

import string

def react_polymers2(x):
    letters = {letter: 0 for letter in string.ascii_lowercase}
    for letter in string.ascii_lowercase:
        x = read_input("data/5-1.txt")
        nx = x.replace(letter, "").replace(letter.capitalize(), "")
        nx = react_polymers(nx)
        letters[letter] = len(nx)
    x = list(letters.items())
    x = [(x[1], x[0]) for x in x]
    x.sort()
    return x
    
x = read_input("data/5-1.txt")
x = react_polymers2(x)

"The answer is: {}".format(x[0][0])