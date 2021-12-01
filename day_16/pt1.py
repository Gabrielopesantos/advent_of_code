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


invalids = 0
for p in nt:
    inv = any([True if check_inv(int(x)) else False for x in p])
    
    if inv:
        invalids += 1

#print(invalids, len(nt), invalids/len(nt))
print(global_counter)
