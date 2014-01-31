import sys, re

if __name__ == "__main__":
    r = re.compile(r'^[a-zA-Z]{1}[_a-zA-Z\d]*@[a-zA-Z]+.[a-zA-z]+$')
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        if r.match(line):
            print "true"
        else:
            print "false"

    FILE.close()
