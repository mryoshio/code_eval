import sys

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(';')
        string = sep[0]
        f_r = sep[1].split(',')
        replaces = []
        for i in range(0, len(f_r), 2):
            print replaces
            string = string.replace(f_r[i], f_r[i+1])
            replaces.append(f_r[i+1])


    FILE.close()

if __name__ == "__main__":
    main()
