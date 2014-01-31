import sys

class Node:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
        self.visited = False
    def __str__(self):
        return "[%d, %s, %s]" % (self.idx, self.val, self.visited)

def depth_first_search(nodes):
    l = []
    prev = nodes[0]
    for node in nodes[1:]:
        if prev.idx < node.idx:
            l.append(node)
    for e in l:
        print e,

def search(q, hits):
    while len(q) > 0:
        list = q.pop(0)
        prev = list.pop()
        print q
        for i, v in enumerate(hits):
            if prev < v:
                print q
#                q.append(list.extend([prev, v]))
                q.append([prev, v])
                search(q, hits[i:])
#            else:
#                q.append(list.extend([prev]))

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(';')
        left = sep[0] ; right = sep[1]
#        nodes = [Node(right.find(s), s) for s in left]
        hits = [right.find(s) for s in left]
        traverse([], hits)


    FILE.close()

if __name__ == "__main__":
    main()
