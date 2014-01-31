import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        print line
    FILE.close()

if __name__ == "__main__":
    main()
