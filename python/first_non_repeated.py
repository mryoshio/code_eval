import sys, re

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        l = []
        for s in line:
            if s in l:
                l.remove(s)
            else:
                l.append(s)
        print l[0]
    FILE.close()

if __name__ == "__main__":
    main()
