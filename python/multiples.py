import sys

def get_multiple(x, n):
    i = 1
    while x > n*i:
        i+=1
    return n*i

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(',')
        print get_multiple(int(sep[0]), int(sep[1]))
    FILE.close()

if __name__ == "__main__":
    main()
