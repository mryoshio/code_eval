import sys, re

r = re.compile(r'\s')
cnt = 0;

def is_palindromic(i):
    str_i = str(i)
    if len(str_i) < 2: return True
    if str_i == str_i[::-1]:
        return True
    return False

def make_list(list, rests):
    print list, rests
    if len(rests) == 0:
        global cnt
        cnt+=len(list)
#        if len(list) % 2 == 0:
#            global cnt
#

    for i,v in enumerate(rests):
        if is_palindromic(v):
            list.append(v)
        make_list(list, rests[i+1:])

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = r.split(line)
        left = int(sep[0]) ; right = int(sep[1])
        list = range(left, right+1, 1)
        for i,v in enumerate(list):
            if is_palindromic(v):
                l = [v]
            else:
                l = []
            make_list(l, list[i+1:])
    print "answer: ", cnt

    FILE.close()

if __name__ == "__main__":
    main()
