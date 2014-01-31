import sys


def permutate(q, length, string, permutates):
    if len(q) == length:
        if not q in permutates:
            permutates.append(q)
        return
    for s in string:
        copy = q[:]
        copy.append(s)
        permutate(copy, length, string, permutates)

if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(',')
        permutates = []
        permutate([], int(sep[0]), sep[1], permutates)
        permutates.sort()
        print ','.join([''.join(ele) for ele in permutates])

    FILE.close()
