import sys

def calculate(val, cnt):
    if val == val[::-1]:
        print cnt, val
        return
    else:
        new_val = int(val) + int(val[::-1])
        cnt += 1
        calculate(str(new_val), cnt)

if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        calculate(line, 0)

    FILE.close()
