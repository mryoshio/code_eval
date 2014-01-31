import re, sys

r = re.compile(r'\s')

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        l = []
        line = r.split(line.strip())
        if line == []: continue
        for s in line:
            l.append(s)
        cnt = 0;
        while len(l) > 0:
            v = l.pop()
            if cnt%2 == 0:
                print v,
            cnt+=1
        print
    FILE.close()

if __name__ == "__main__":
    main()
