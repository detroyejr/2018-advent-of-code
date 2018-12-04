"""
Day 2
"""

# Part 1
def read_input(x):
    x = open(x).readlines()
    x = [x.replace("\n", "") for x in x]
    x = [x.replace("+", "") for x in x]
    return x


def appears_twice(x):
    counter = 0
    for v in x:
        for i in set(v):
            n = v.count(i)
            if n == 2:
                counter += 1
                break
    return counter


def appears_three(x):
    counter = 0
    for v in x:
        for i in set(v):
            n = v.count(i)
            if n == 3:
                counter += 1
                break
    return counter


def get_answer(x):
    twice = appears_twice(x)
    three = appears_three(x)
    res = twice * three
    return res


x = read_input("data/2-1.txt")
"The answer is: {}".format(get_answer(x))

# Part 2


def match(x):
    n = len(x[0])
    r = list(range(0, n))
    for i in r:
        res = []
        for v in x:
            v = list(v)
            v.pop(i)
            v = "".join(v for v in v)
            res += [v]
        for r in res:
            f = res.count(r)
            if f == 2:
                return r


x = read_input("data/2-1.txt")
"The answer is: {}".format(match(x))
