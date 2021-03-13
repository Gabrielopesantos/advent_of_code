def plusone(v, l=""):
    l += f"{v}"
    if v > 99:
        pass 
    else:
        l += plusone(v+1, l)

    return l

#print(plusone(1))
from itertools import combinations

print(list(combinations((0, 1), 3)))
