import sys, re

r = re.compile(r'\s')

def get_values(line):
    line = line.strip()
    if line == '':
        return []
    else:
        return r.split(line.strip())

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        vals = get_values(line)
        if vals == []: continue
        v = vals[0]
        for s in vals[1:]:

        print
    FILE.close()


if __name__ == "__main__":
    main()
