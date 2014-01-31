import sys

# XMJYAUZ;MZJAWXU
# => [0, 1, 2, 3, 4, 5, 6];[1, 6, 2, 4, -1, 0, 5]
longest = []

def print_longest(current, rest):
    global longest
    if len(current) + len(rest) <= len(longest) : return
    if len(rest) == 0:
        if len(current) > len(longest):
            longest = current
    for i,v in enumerate(rest):
        copy = current[:]
        if copy[-1] < v:
            copy.append(v)
        print_longest(copy, rest[i+1:])

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        global longest
        longest = []
        line = line.strip()
        if line == '': continue
        sep = line.split(';')
        l = [(-1)]*len(sep[1])
        for i,v in enumerate(sep[0]):
            if sep[1].find(v) > -1:
                l[sep[1].find(v)] = i
        for i,v in enumerate(l):
            if v == -1: continue
            print_longest([v], l[i+1:])

        print ''.join([sep[0][v] for v in longest])
    FILE.close()

if __name__ == "__main__":
    main()
