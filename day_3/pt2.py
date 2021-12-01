import math

with open("input.txt", "r") as f:
    mntn = list(x.strip() for x in f.readlines())

trees_list = []
cases = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for r, d in cases:
    col = 0
    trees = 0
    for i in range(0, len(mntn), d):
        row = mntn[i]
         
        if col < 31:
            if row[col] == "#":
                trees += 1
        else:
            rst = col % 31
            if row[rst] == "#":
                trees += 1
        
        col += r
    trees_list.append(trees)

#print(trees_list)
print(math.prod(trees_list))
