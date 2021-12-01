from itertools import combinations

def pt1(l):

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 2020:
                return l[i] * l[j] 

def pt2(l):

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for w in range(i+1, len(l)):
                if l[i] + l[j] + l[w] == 2020:
                    return l[i] * l[j] * l[w]

def pt1_2_alt(l):

    # easily adaptable to pt1    

    for (i, j, w) in combinations(l, 3):
        if i + j + w == 2020:
            return i * j * w

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        l = list(map(int, f.readlines()))

        res1 = pt1(l)
        print(f"Pt1 {res1}")

        res2 = pt2(l)
        print(f"Pt2 {res2}")

        print(pt1_2_alt(l))
