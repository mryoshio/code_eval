import sys

tel_map = {'0':['0'], '1':['1'], '2':['a', 'b', 'c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

def get_words(q, string, words, original):
    if len(q) + len(string) != len(original):
        return
    if string == '':
        words.append(q)
        return
    for i, s in enumerate(string):
        for v in tel_map[s]:
            copy = q[:]
            copy.append(v)
            get_words(copy, string[i+1:], words, original)

if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        words = []
        get_words([], line, words, line)
        words.sort()
        print ','.join([''.join(ele) for ele in words])

    FILE.close()
