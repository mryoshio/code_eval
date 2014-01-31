import sys

def search_repeated(list, string, line, matchs, max):
    for i, s in enumerate(string):
        l = list[:]
        t = ''.join(l)
        if t*2 in line:
            if not t in matchs:
                if len(t) > max:
                    max = len(t)
                    if len(matchs) == 0:
                        matchs.append(t)
                    elif len(t) > len(matchs[len(matchs)-1]):
                        matchs.append(t)
                    else:
                        return
        if len(string[i+1:]) > max*2:
            l.append(s)
            search_repeated(l, string[i+1:], line, matchs, max)
        else:
            return

def print_max(matchs):
    if len(matchs) == 0:
        print "NONE"
    else:
        max = ''
        for m in matchs:
            if len(m) > len(max):
                max = m
        print max

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        matchs = []
        line = line.strip()
        if line == '': continue
        for i, s in enumerate(line):
            search_repeated([s], line[i+1:], line, matchs, 0)
        print_max(matchs)
    FILE.close()

if __name__ == "__main__":
    main()
