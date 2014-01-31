import sys, re

if __name__ == "__main__":
    r = re.compile(r"\s")
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = r.split(line)
        sep.reverse()
        for word in sep:
            print word,
        print
    FILE.close()
