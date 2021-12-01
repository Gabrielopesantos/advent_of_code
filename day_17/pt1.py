from collections import Counter

n_cycles = 6

with open("d17input.txt", "r") as f:
    m = [list(x.strip()) for x in f.readlines()]

#m = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]

def get_marked_pos(m):
    return {(0, x, y) for x, line in enumerate(m) for y, c\
        in enumerate(line) if c=="#"}

marked_positions = get_marked_pos(m)

while n_cycles != 0:
    nmarked = Counter()

    for p in marked_positions:
        for z in (-1, 0, 1):
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    if z == x == y == 0:
                        continue
                    else:
                        nmarked[(p[0] + z, p[1] + x, p[2] + y)] += 1
    
    n_marked_positions = set()
    for k,v in nmarked.items():
        if v == 3:
            n_marked_positions.add(k)

    for k in marked_positions:
        if nmarked[k] in (2, 3):
            n_marked_positions.add(k)

    marked_positions = n_marked_positions
    n_cycles -= 1

print(len(marked_positions))
