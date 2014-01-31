import sys, re
from math import fabs

r = re.compile(r'\s')

def judge(nums):
    diffs = []
    for i in range(len(nums)-1):
        diffs.append(fabs(nums[i+1]-nums[i]))
    diffs.sort()
    for i in range(len(diffs)-1):
        if diffs[i+1] != diffs[i]+1:
            print "Not jolly"
            return
    print "Jolly"

if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '':continue
        nums = r.split(line)
        judge([int(x) for x in nums])
    FILE.close()
