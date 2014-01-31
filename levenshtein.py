import sys, re

def make_add(word):
    regexs = []
    for i, s in enumerate(word):
        regexs.append(re.compile(r'^' + word[:i] + "\S{1}" + word[i:] + '$'))
    regexs.append(re.compile(r'^\S{1}' + word + '$'))
    regexs.append(re.compile(r'^' + word + '\S{1}$'))
    return regexs

def make_remove(word):
    regexs = []
    former = ''
    for i, s in enumerate(word):
        regexs.append(re.compile(r'^' + former + word[i+1:] + '$'))
        former+=s
    return regexs

def make_substitution(word):
    regexs = []
    former = ''
    for i, s in enumerate(word):
        regexs.append(re.compile(r'^' + former + "\S{1}" + word[i+1:] + '$'))
        former+=s
    return regexs

def get_socialnetwork(file, words, friends, depth):
    file.seek(0)
    rs = []
    for word in words:
        rs+=make_add(word)
        rs+=make_remove(word)
        rs+=make_substitution(word)
    words = []
    for line in file:
        line = line.strip()
        for r in rs:
            if r.match(line):
                if line in friends:
#                    print line, words
                    pass
                else:
                    friends.append(line)
                    words.append(line)
    if len(words) == 0:return
    depth+=1
    get_socialnetwork(file, words, friends, depth)
if __name__ == "__main__":
    file = open(sys.argv[1], 'r')
    friends = []
#    get_socialnetwork(file, ["hello"], friends, 0)
    get_socialnetwork(file, ["causes"], friends, 0)
#    get_socialnetwork(file, ["abcde"], friends, 0)
    print len(friends)
#    print friends
    file.close()
