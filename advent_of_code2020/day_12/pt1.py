import itertools

l = ["F10", "N3", "F7", "R90", "F11"]

with open("input.txt", "r") as f:
    l = [x.strip() for x in f.readlines()]

DIRECTIONS = [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0),
        ]
x = 0
y = 0
direction = DIRECTIONS[0]

for act in l:
    d, n = act[0], int(act[1:])

    if d == "N":
        y += n
    elif d == "S":
        y -= n
    elif d == "E":
        x += n
    elif d == "W":
        x -= n
    elif d == "L":
        rotations = n // 90
        ind = DIRECTIONS.index(direction)
        direction = DIRECTIONS[(ind - rotations) % 4]

    elif d == "R":
        rotations = n // 90
        ind = DIRECTIONS.index(direction)
        direction = DIRECTIONS[(ind + rotations) % 4]

    elif d == "F":
        x += n * direction[0]
        y += n * direction[-1]

print(abs(x) + abs(y))
