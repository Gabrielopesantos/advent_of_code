
    # pt1

def pt1(l):
    valid = 0 
    for n, c, pwd in l:
        mi, ma = list(map(int, n.split('-')))

        num_c = sum([1 if x == c else 0 for x in pwd])

        if mi <= num_c <= ma:
            valid += 1
    return valid

def pt2(l):
    valid = 0
    for n, c, pwd in l:
        p1, p2 = list(map(int, n.split('-')))

        s = sum([1 if pwd[x-1] == c else 0 for x in [p1, p2]])

        if s == 1:
            valid += 1

    return valid


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [(line.split(" ")[0], line.split(":")[0][-1], 
            line.split(":")[-1].strip()) for line in f.readlines()]
        
        res1 = pt1(l)
        print(f"pt1 {res1}")

        res2 = pt2(l)
        print(f"pt2 {res2}")
