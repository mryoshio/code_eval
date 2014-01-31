import sys


def permutate(q, string, permutates):
    if string == '':
        permutates.append(q)
        return
    for s in string:
        copy = q[:]
        copy.append(s)
        permutate(copy, string.replace(s, '', 1), permutates)

if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        permutates = []
        permutate([], line, permutates)
        permutates.sort()
        print ','.join([''.join(ele) for ele in permutates])

    FILE.close()
