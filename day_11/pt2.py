from itertools import combinations

with open("input.txt", "r") as f:
    l = [list(x.strip()) for x in f.readlines()]

tot_rows = len(l)
tot_cols = len(l[0])

def seats_around2(pos: tuple, l:list):
    row, col = pos
                    # top, bottom, left, right, upper_right, upper_left, down_right, down_left
    combinations =  (-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)
    seats_occupied = 0
    
    for x, y in combinations:
        cur_x, cur_y = row, col
        while True:
            cur_x, cur_y = cur_x + x, cur_y + y
            if tot_rows - 1 < cur_x or cur_x < 0 or tot_cols - 1 < cur_y or cur_y < 0:
                break
            if l[cur_x][cur_y] == "#":
                seats_occupied += 1
                break
            elif l[cur_x][cur_y] == "L":
                break

    return seats_occupied

prev = 0

while True:

    new_l = []
    tot_oc_seats = 0

    for x in range(len(l)):
        new_row = []
        for y in range(len(l[x])):
            if l[x][y] == ".":
                new_row.append(".")
            elif seats_around2((x, y), l) > 4 and l[x][y] == "#" or seats_around2((x, y), l) > 0 and l[x][y] == "L": 
                new_row.append("L")
            elif seats_around2((x, y), l) == 0 and l[x][y] == "L" or l[x][y] == "#" and seats_around2((x, y), l) < 5:
                new_row.append("#")
        new_l.append(new_row)

    tot_oc_seats = sum([1 if x == "#" else 0 for row in new_l for x in row])
    #print(tot_oc_seats)
    if prev == tot_oc_seats:
        print(tot_oc_seats)
        break
    prev = tot_oc_seats

    l = new_l
