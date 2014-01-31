import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        d = {}
        l = line.split(';')[1].split(',')
        for val in l:
            if val in d.keys():
                print val
            else:
                d[str(val)] = 1
    FILE.close()

if __name__ == "__main__":
    main()
