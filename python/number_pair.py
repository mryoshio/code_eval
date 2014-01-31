import sys

def calculate(nums, sum):
    lists = []
    for i, n1 in enumerate(nums):
        if i < len(nums)-1:
            for n2 in nums[i+1:]:
                if n1 + n2 == sum:
                    lists.append([str(n1),str(n2)])
    if lists == []:
        print "NULL"
    else:
        print ';'.join([','.join(x) for x in lists])

if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(';')
        calculate([int(s) for s in sep[0].split(',')], int(sep[1]))

    FILE.close()
