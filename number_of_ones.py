import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        bin_num = bin(int(line))[2:]
        print bin_num.count('1')
    FILE.close()

if __name__ == "__main__":
    main()
