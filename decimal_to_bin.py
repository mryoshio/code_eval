import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(',')
        if sep[0].endswith(sep[1]):
            print 1
        else:
            print 0
    FILE.close()

if __name__ == "__main__":
    main()
