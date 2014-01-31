import sys

def check_self_describing_numbers(string):
    for idx, s in enumerate(string):
        if string.count(str(idx)) != int(s):
            return False
    return True

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        if check_self_describing_numbers(line):
            print 1
        else:
            print 0
    FILE.close()

if __name__ == "__main__":
    main()
