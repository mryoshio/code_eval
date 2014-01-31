import sys

def permutate(q, string, permutates):
    if string == '':
        permutates.append(q)
        return
    for s in string:
        copy = q[:]
        copy.append(s)
        permutate(copy, string.replace(s, '', 1), permutates)

def get_strs(length, str):
    print str
    strs = []
    for i in range(0, len(str)-1):
        s = set([str[i]])
        for j in range(i+1, len(str)):
            s.add(str[j])
            if len(s) == length and not s in strs:
                strs.append(s)
    return strs

if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(',')
        length = int(sep[0])
        str_list = sep[1]
        strs = get_strs(int(sep[0]), sep[1])
        permutates = []
        for str in strs:
            permutate([], ','.join(str), permutates)
            permutates.sort()
#        print ','.join([''.join(ele) for ele in permutates])
    FILE.close()
