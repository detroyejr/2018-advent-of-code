"""
Day 3
"""

# Part 1
import re
import itertools

def read_input(x):
    x = open(x).readlines()
    x = [x.replace("\n", "") for x in x]
    x = [x.replace("+", "") for x in x]
    return x

x = ["#1 @ 1,3: 4x4",
"#200 @ 3,1: 4x4",
"#3 @ 4,4: 3x3"]

def overlap(x):
    x = [re.findall(r"\d+", string=v)[1:] for v in x]
    x = [list(map(int, x)) for x in x]
    r = []
    for j, k, l, m in x:
        r += [(range(j, j + l), range(k, k + m))]
    x = list(itertools.combinations(r, 2))
    counter = 0
    xo = []
    xp = []
    for  j, k in x:
        o = [i in k[0] and i not in xo for i in list(j[0])]
        p = [i in k[1] and i not in xp for i in list(j[1])]
        n = sum(o) * sum(p)
        if n > 0:
            xo += itertools.compress(list(j[0]), o)
            xp += itertools.compress(list(j[1]), p)
        counter += n

    return counter


overlap(x)


x = read_input("data/3-1.txt")
overlap(x)

