import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        sum = 0
        if line == '':continue
        for w in str(line):
            sum += int(w)
        print sum
    FILE.close()

if __name__ == "__main__":
    main()
