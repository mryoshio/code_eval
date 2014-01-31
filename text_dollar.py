import sys

NUMS = [[100, 'OneHundred'], [90, 'Ninety'], [80, 'Eighty'], [70, 'Seventy'], [60, 'Sixty'], [50, 'Fifty'], [40, 'Forty'], [30, 'Thirty'], [20, 'Twenty'], [19, 'Nineteen'], [18, 'Eighteen'], [17, 'Seventeen'], [16, 'Sixteen'], [15, 'Fifteen'], [14, 'Fourteen'], [13, 'Thirteen'], [12, 'Twelve'], [11, 'Eleven'], [10, 'Ten'], [9, 'Nine'], [8, 'Eight'], [7, 'Seven'], [6, 'Six'], [5, 'Five'], [4, 'Four'], [3, 'Three'], [2, 'Two'], [1, 'One']]

DIJITS = [[1000000000, 'Billion'], [1000000, 'Million'], [1000, 'Thousand'], [100, 'Hundred'], [1, 'One']]

def make_text_expression(num):
    if num == 0: return ["Zero"]
    str_list = []
    for d in DIJITS:
        for n in NUMS:
            if num/(n[0]*d[0]) > 0:
                num -= n[0]*d[0]
                if d[0] == 1:
                    str_list += [n[1]]
                else:
                    str_list += [n[1], d[1]]
            if num == 0: return str_list

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        text = make_text_expression(int(line))
        if len(text) == 1 and text[0] in ('One', 'Zero'):
            print text[0] + "Dollar"
        else:
            print ''.join(text) + "Dollars"
    FILE.close()

if __name__ == "__main__":
    main()
