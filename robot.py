from copy import deepcopy

DIRECTIONS = ["up", "down", "left", "right"]
MAX_X = 4 ; MAX_Y = 4
cnt = 0

def make_board():
    list = []
    for r in range(MAX_Y):
        l = []
        for c in range(MAX_X):
            l.append(0)
        list.append(l)
    return list

def is_goal(x, y):
    return x==3 and y==3

def move_robot(list, x, y, direction):
    list[x][y] +=1
    if direction == "up":
        if y < MAX_Y-1 and list[x][y+1] < 1:
            y+=1
        else:
            return
    elif direction == "down":
        if 0 < y and list[x][y-1] < 1:
            y-=1
        else:
            return
    elif direction == "left":
        if 0 < x and list[x-1][y] < 1:
            x-=1
        else:
            return
    elif direction == "right":
        if x < MAX_X-1 and list[x+1][y] < 1:
            x+=1
        else:
            return
    if is_goal(x, y):
        global cnt ; cnt+=1
        return
    for d in DIRECTIONS:
        l_copy = deepcopy(list)
        move_robot(l_copy, x, y, d)

if __name__ == "__main__":
    list = make_board()
    for d in DIRECTIONS:
        l_copy = deepcopy(list)
        move_robot(l_copy, 0, 0, d)
    print cnt
