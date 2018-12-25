"""
Day 6
"""

def read_input(x):
    x = open(x).readlines()
    x = [x.replace("\n", "") for x in x]
    x = [x.replace("+", "") for x in x]
    x = [tuple(x.split(", ")) for x in x]
    x = [(int(x[0]), int(x[1])) for x in x]
    return x


x = read_input("data/6-1.txt")
x.sort()

top = range((min(x[0] for x in x)), max(x[0] for x in x))
bottom = range((min(x[1] for x in x)), max(x[1] for x in x))

loc = []
for t in top:
    for b in bottom:
        loc += [(t, b)]

res = []
for v in x:
    for l in loc:
        res += [(v[0] - l[0], v[1] - l[1])]