import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(',')
        string = sep[0].strip()
        scrubbed = sep[1].strip()
        l = []
        for s in string:
            if not s in scrubbed:
              l.append(s)
        print ''.join(l)
    FILE.close()

if __name__ == "__main__":
    main()
