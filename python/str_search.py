import sys, re

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = [ x.strip() for x in line.split(',')]
        r = re.compile(sep[1])
        if r.search(sep[0]):
            print "true"
        else:
            print "false"
    FILE.close()

if __name__ == "__main__":
    main()
