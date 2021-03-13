from itertools import combinations

f = "input.txt"
with open(f, "r") as f:
    l = [list(x.strip()) for x in f.readlines()]

tot_rows = len(l)
tot_cols = len(l[0])

def seats_around(pos: tuple, l):
    row, col = pos
    occupied_seats = 0

    combs = list(set(combinations([row - 1, row + 1, row, col, col - 1, col + 1], 2)))
    combs.remove(pos)
    combs = [(x[0], x[1]) for x in combs if -1 < x[0] < tot_rows and -1 < x[1] < tot_cols]
    combs = [(x[0], x[1]) for x in combs if abs(x[0] - pos[0]) + abs(x[1] - pos[1]) <= 2]
    
    #print(combs)
    for x, y in combs:
        if l[x][y] == "#":
            occupied_seats += 1

    return occupied_seats

prev = 0

while True:
    new_l = []
    tot_oc_seats = 0
    for x in range(len(l)):
        new_row = []
        for y in range(len(l[x])):
            if l[x][y] == ".":
                new_row.append(".")
            elif seats_around((x, y), l) > 3 and l[x][y] == "#" or seats_around((x, y), l)  > 0 and l[x][y] == "L":
                new_row.append("L")
            elif seats_around((x, y), l) == 0 and l[x][y] == "L" or l[x][y] == "#" and seats_around((x, y), l) < 4:
                new_row.append("#")
        new_l.append(new_row)

    tot_oc_seats = sum([1 if x == "#" else 0 for row in new_l for x in row])
    if prev == tot_oc_seats:
        print(tot_oc_seats)
        break
    prev = tot_oc_seats

    l = new_l
