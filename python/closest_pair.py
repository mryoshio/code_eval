import sys, re
from math import hypot

MAX_DISTANCE = 10000
r = re.compile(r'\s')

def calculate(pairs):
    if pairs == []:return
    min_distance = MAX_DISTANCE
    for i, p1 in enumerate(pairs):
        if i < len(pairs)-1:
            for p2 in pairs[i+1:]:
                d = hypot(p1[0]-p2[0], p1[1]-p2[1])
                if d < min_distance:
                    min_distance = d
    if min_distance < MAX_DISTANCE:
        print "%6.4f" % min_distance
    else:
        print "INFINITY"

if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '':
            continue
        if line == '0':
            calculate(pairs)
            pairs = []
        else:
            pair = r.split(line)
            if len(pair) == 1:
                pairs = []
            else:
                pairs.append([int(x) for x in pair])
    FILE.close()




