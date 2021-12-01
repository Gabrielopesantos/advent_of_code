with open("input.txt", "r") as f:
    _, seq = [x.strip() for x in f.readlines()]


seq = tuple((int(x), i) for i, x in enumerate(seq.split(",")) if x != "x")

t = 0
mult = seq[0][0]

for bus, pos in seq[1:]:
    while (t + pos) % bus != 0:
        t += mult
    mult *= bus
print(t)
