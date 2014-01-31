import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        l = []
        clusters = line.split(';')
        former = clusters[0].split(',')
        latter = clusters[1].split(',')
        for s in former:
            if s in latter:
                l.append(s)
        print ','.join(l)
    FILE.close()

if __name__ == "__main__":
    main()
