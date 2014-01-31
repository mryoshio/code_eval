import sys

def is_bits_same(num, pos1, pos2):
    if pos1 == pos2: return "true"
    bits_str = bin(num)[2:]
    if bits_str[-pos1] == bits_str[-pos2]:
        return "true"
    else:
        return "false"

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(',')
        print is_bits_same(int(sep[0]), int(sep[1]), int(sep[2]))
    FILE.close()

if __name__ == "__main__":
    main()
