import sys, re


def calculate(list):

    if len(list) == 1:
        return list.pop()

    ops = ["+", "*", "/"]
    stack = []

    for ele in list:
        if ele in ops:
            stack.append(ele)
            continue
        ele = int(ele)
        popped = stack.pop()
        if popped in ops:
            stack.extend([popped, ele])
        else:
            op = stack.pop()
            if op == "+":
                result = popped+ele
            elif op == "*":
                result = popped*ele
            elif op == "/":
                result = popped/ele
            stack.append(result)
    return calculate(stack)

if __name__ == "__main__":
    r = re.compile(r'\s')
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = r.split(line)
        print calculate(sep)
    FILE.close()
