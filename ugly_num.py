import sys


def create_num(q, string, numbers):
    if string == '':
        numbers.append(q)
        return
    for s in string:
        copy = q[:]
        copy.append(s)
        create_num(copy, string.replace(s, '', 1), permutates)



if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        numbers
#        create_num([], line, permutates)
        l = []
        for i, s in enumerate(line):
            l.append(s)
            create_num(int(''.join(l)), line[i+1:], numbers)
        print permutates

    FILE.close()
