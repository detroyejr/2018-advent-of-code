"""
Day 01
"""

# Part 1.
def read_input(x):
    x = open(x).readlines()
    x = [x.replace("\n", "") for x in x]
    x = [x.replace("+", "") for x in x]
    x = [int(x) for x in x]
    return x

x = read_input("data/1-1.txt")
"The Answer is: {}".format(sum(x))

# Part 2.
def repeats_twice(x):
    v, r = 0, []
    for i in (x * 1000):
        v += i
        if v in r:
            break
        r += [v]
    return v


x = read_input("data/1-1.txt")
"The Answer is: {}".format(repeats_twice(x))
