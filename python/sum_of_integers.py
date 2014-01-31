import sys

def get_max_from_list(list):
    max = -sys.maxint-1
    sum = 0
    for i in range(0, len(list)):
        sum += int(list[i])
        if max < sum:
            max = sum
    return max

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '':continue
        max = -sys.maxint-1
        nums = line.split(',')
        for i in range(0, len(nums)):
            l_max = get_max_from_list(nums[i:])
            if max < l_max:
                max = l_max
        print max
    FILE.close()

if __name__ == "__main__":
    main()
