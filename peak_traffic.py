import sys, re

clusters = []
r = re.compile(r'\s')

def make_cluster(mail1, mail2):

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
        sep = r.split(line)
#        print sep
        make_cluster(sep[9], sep[13])
#        print ','.join([''.join(ele) for ele in permutates])

    FILE.close()
