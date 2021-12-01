import itertools

#l = ["F10", "N3", "F7", "R90", "F11"]

with open("input.txt", "r") as f:
    l = [x.strip() for x in f.readlines()]

DIRECTIONS = [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0),
        ]
s_x = 0
s_y = 0
w_x = 10
w_y = 1

direction = DIRECTIONS[0]

for act in l:
    d, n = act[0], int(act[1:])

    if d == "N":
        w_y += n
    elif d == "S":
        w_y -= n
    elif d == "E":
        w_x += n
    elif d == "W":
        w_x -= n
    elif d == "L":
        for _ in range(n // 90):
            w_x, w_y = w_y, w_x
            w_x = -w_x

    elif d == "R":
        for _ in range(n // 90):
            w_x, w_y = w_y, w_x
            w_y = - w_y

    elif d == "F":
        s_x += n * w_x
        s_y += n * w_y

#print(s_x, s_y)
print(abs(s_x) + abs(s_y))
