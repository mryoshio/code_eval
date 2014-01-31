import sys, re

def fizzbuzz(f, b, till):
    for cnt in range(1, till):
        if (cnt%f==0) and (cnt%b==0):
            print "FB",
        elif cnt % f == 0:
            print "F",
        elif cnt % b == 0:
            print "B",
        else:
            print cnt,
    print

if __name__ == "__main__":
    r = re.compile(r"\s")
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        sep = r.split(line.strip())
        fizzbuzz(int(sep[0]), int(sep[1]), int(sep[2])+1)
    FILE.close()
