"""
Day 7
"""

from collections import namedtuple

def read_input(x):
    x = open(x).readlines()
    x = [x.replace("\n", "") for x in x]
    x = [x.replace("+", "") for x in x]
    return [(x[5], x[-12]) for x in x]


x = read_input("data/7-1.txt")


r = set([x for x in [[x[0], x[1]] for x in x] for x in x])

r = {l: len(r) for l in r}

for j, k in x:
    if r.get(j) >= r.get(k)
    r.get(j) = r.get(k) - 1
