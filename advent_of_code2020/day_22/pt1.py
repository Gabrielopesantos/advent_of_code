
with open("d22input.txt", "r") as f:
    p1, p2 = [list(map(int, x.strip().split("\n")[1:])) for x in f.read().split("\n\n")]

while True:
    if len(p1) == 0 or len(p2) == 0:
        break

    p1t = p1.pop(0)
    p2t = p2.pop(0)

    if p1t > p2t:
        p1.extend([p1t, p2t])
    else:
        p2.extend([p2t, p1t])

highest_score = max(sum([val * mult for mult, val in zip(range(1, len(p)+1),\
        p[::-1])]) for p in [p1, p2])
print(highest_score)
