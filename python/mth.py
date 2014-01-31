import re, sys

r = re.compile(r'\s')

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        l = []
        line = line.strip()
        if line == '': continue
        line = r.split(line)
        for s in line:
            l.append(s)
        idx = int(l.pop())-1
        if len(l) <= idx:
            continue
        l.sort(reverse=True)
        print l[idx]
    FILE.close()

if __name__ == "__main__":
    main()
