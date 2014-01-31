import sys, re

def init_dictionary():
    dic = {}
    for s in range(ord('a'), ord('z')+1):
        dic[chr(s)] = 0
    return dic

def output(dic):
    l = []
    keys = dic.keys()
    keys.sort()
    for k in keys:
        if dic[k] == 0: l.append(k)
    if len(l) == 0:
        print "NULL"
    else:
        print ''.join(l)

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip().lower()
        if line == '': continue
        dic = init_dictionary()
        for s in line:
            if s.isalpha():
                dic[s] += 1
        output(dic)
    FILE.close()

if __name__ == "__main__":
    main()
