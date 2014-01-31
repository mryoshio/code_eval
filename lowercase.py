import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        words = line.split(',')
        for w in words:
            print w.lower(),
        print
    FILE.close()

if __name__ == "__main__":
    main()
