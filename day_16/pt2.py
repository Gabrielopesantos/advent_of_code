f = "d16input.txt"
#f = "example.txt"
with open(f, "r") as f:
    data = f.read()

rules, mt, nt = [x for x in data.split("\n\n")]

urules = [(x.split(":")[0], x.split(":")[-1].strip()) for x in rules.split("\n")]
nt = [x.split(",") for x in nt.split("\n")[1:-1]]

global_counter = 0

def check_inv(val):
    global global_counter

    check = False
    for rn, rv in urules:
        r1, r2  = rv.split(" or ")
        
        if int(r1.split("-")[0]) <= val <= int(r1.split("-")[-1]) \
                or int(r2.split("-")[0]) <= val <= int(r2.split("-")[-1]):
            check = False
            break
        else:
            check = True
    
    if check:
        global_counter += val
    return check


def check_n(val, rules):
    r1, r2 = rules.split(" or ")
    check = False
    if int(r1.split("-")[0]) <= val <= int(r1.split("-")[-1]) \
                or int(r2.split("-")[0]) <= val <= int(r2.split("-")[-1]):
        check = True
        #print(rules, val, check, sep="\n")

    return check

invalids = 0
valids = []
for p in nt:
    inv = any([True if check_inv(int(x)) else False for x in p])

    if not inv:
        valids.append(p)

# aqui

tot_rules = []
for r_name, numbers in urules:
    c_rule = []
    for i in range(0, len(urules)):
        #print([True if check_n(int(x[0]), numbers) else False for x in valids])
        c_rule.append(all(True if check_n(int(x[i]), numbers) else False for x in valids))
    tot_rules.append([r_name, sum([1 if x == True else 0 for x in c_rule]), [i for i, x in enumerate(c_rule) if x == True], c_rule])

tot_rules.sort(key=lambda x: x[1])
lst_idxs = tot_rules[0][2]
mult = 1
mt_vals = mt.split("\n")[-1].split(",")
for t in tot_rules[1:]:
    #print(t)
    idx = set(t[2]) - set(lst_idxs)
    if t[0].startswith("dep", 0, 3):
        mult *= int(mt_vals[list(idx)[0]])
    #print(t[0], idx)
    lst_idxs = t[2]
print(mult)
"""
tot_rules = [(sum(1 if x == True else 0 for x in t), t, r[0]) for t, r in zip(tot_rules, urules)]

tot_rules.sort(key=lambda x: x[0])
idxs = []
for t in tot_rules:
    idxs.append([t[-1], [i for i, x in enumerate(t[1]) if x == True]])

lst = idxs[0][-1]
mult = 1
mt_vals = mt.split("\n")[-1].split(",")
for n, t in idxs[1:]:
    #print(lst, t)
    un = set(t) - (set(lst))
    if n.startswith("dep", 0, 3):
        print(n)
        mult *= int(mt_vals[list(un)[0] - 1])
    print(un, n)
    lst = t

print(mt)
print(mult)
"""
