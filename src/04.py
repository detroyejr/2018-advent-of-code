"""
Day 4
"""

import re
import datetime

def read_input(x):
    x = open(x).readlines()
    x = [x.replace("\n", "") for x in x]
    x = [x.replace("+", "") for x in x]
    return x

def parse_datetime(x):
    x = [re.findall(pattern=r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", string=x)[0] for x in x]
    x = [datetime.datetime.strptime(x, "%Y-%m-%d %H:%M") for x in x]
    return x

def parse_messages(x):
    return [x.split("] ")[1] for x in x]

def parse_guard(x):
    res = []
    for x in x:
        if x.find("#") > 0:
            sid = re.findall(r"#(\d+)", x)[0]
            res += [sid]
        else:
            res += [sid]
    return res

def guard_most_asleep(x):
    dates, messages, guards = parse_datetime(x), parse_messages(x), parse_guard(x)
    x = list(zip(dates, messages, guards))
    x = [x for x in x if "falls asleep" in x[1] or "wakes up" in x[1]]
    r = range(0, 774, 2)
    gd= {x: datetime.timedelta(0) for x in set(guards)}
    for i in r:
        n = x[i + 1][0] - x[i][0]
        sid = x[i][2]
        gd[sid] += n

    gd = list(gd.items())
    gd = [(x[1], x[0]) for x in gd]
    gd.sort()
    return gd[-1][1]

def get_daterange(x, y):
    delta = x - y
    m = []
    for i in range(int(delta.seconds / 60)):
        m += [(y + datetime.timedelta(seconds = i * 60)).minute]
    return m

def part_one(x):
    sid_asleep = guard_most_asleep(x)
    dates, messages, guards = parse_datetime(x), parse_messages(x), parse_guard(x)
    x = list(zip(dates, messages, guards))

    sleep_log = [x for x in x if x[2] == sid_asleep]
    sleep_log = [x for x in sleep_log if "falls asleep" in x[1] or "wakes up" in x[1]]
    r = range(0, len(sleep_log), 2)
    n = []
    for i in r:
        n += get_daterange(sleep_log[i + 1][0], sleep_log[i][0])

    sleep_minutes = [(n.count(x), x) for x in range(0, 60)]
    sleep_minutes.sort()

    return int(sid_asleep) * sleep_minutes[-1][1]


x = read_input("data/4-1.txt"); x.sort()

"The answer is: {}".format(part_one(x))

# Part 2

def guard_most_minutes(x):
    dates, messages, guards = parse_datetime(x), parse_messages(x), parse_guard(x)
    x = list(zip(dates, messages, guards))
    sleep_log = [x for x in x if "falls asleep" in x[1] or "wakes up" in x[1]]
    r = range(0, len(sleep_log), 2)
    gd= {x: [] for x in set(guards)}
    for i in r:
        gd[sleep_log[i][2]] += get_daterange(sleep_log[i + 1][0], sleep_log[i][0])

    for key in gd.keys():
        gd[key] = [(gd[key].count(x), x) for x in range(0, 60)]
        gd[key].sort()
        gd[key] = gd[key][-1]
    return gd

x = read_input("data/4-1.txt"); x.sort()
gm = guard_most_minutes(x)

"The answer is: {}".format(int(list(gm.keys())[-1]) * int(gm[ list(gm.keys())[-1]][1]))