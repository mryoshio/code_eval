import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        num = line
        l = []
        while True:
            sum = 0
            l.append(num)
            for i in num:
                sum += int(i)**2
            if sum == 1:
                print 1
                break;
            elif str(sum) in l:
                print 0
                break
            else:
                num = str(sum)

    FILE.close()

if __name__ == "__main__":
    main()
