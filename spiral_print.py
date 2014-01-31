import sys, re

r = re.compile(r'\s')

def make_board(max_row, max_column, nums):

    list = []
    cnt = 0
    for r in range(max_row):
        l = []
        for c in range(max_column):
            l.append(nums[cnt])
            cnt+=1
        list.append(l)
    return list

def all_is_visited(num_list, r, c):

    try:
        return num_list[r+1][c] == -1 and num_list[r-1][c] == -1 and num_list[r][c+1] == -1 and num_list[r][c-1] == -1
    except:
        return False

def print_spiral(num_list, row, column, row_max, column_max, direction):

    print num_list[row][column],
    num_list[row][column] = -1

    if all_is_visited(num_list, row, column):
        return

    if direction == "right":
        if column < column_max-1 and num_list[row][column+1] != -1:
            column+=1
        else:
            row+=1 ; direction = "down"
    elif direction == "down":
        if row < row_max-1 and num_list[row+1][column] != -1:
            row+=1
        else:
            column-=1 ; direction = "left"
    elif direction == "left":
        if column > 0 and num_list[row][column-1] != -1:
            column-=1
        else:
            row-=1 ; direction = "up"
    elif direction == "up":
        if row > 0 and num_list[row-1][column] != -1:
            row-=1
        else:
            column+=1 ; direction = "right"

    print_spiral(num_list, row, column, row_max, column_max, direction)

def main():
    FILE = open(sys.argv[1], 'r')
    for line in FILE:
        line = line.strip()
        if line == '': continue
        sep = line.split(';')
        row_max = int(sep[0]) ; column_max = int(sep[1])
        nums = r.split(sep[2])
        num_list = make_board(row_max, column_max, nums)
        print_spiral(num_list, 0, 0, row_max, column_max, "right")
        print
    FILE.close()

if __name__ == "__main__":
    main()
