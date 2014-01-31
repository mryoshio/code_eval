import sys

def fibo(n):
    if n in (0, 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        sum = 0
        if line == '':continue
        print fibo(int(line))
    FILE.close()

if __name__ == "__main__":
    main()
