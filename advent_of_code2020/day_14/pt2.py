from itertools import combinations, combinations_with_replacement, permutations,\
product
import copy

#ex_input = "mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1"

with open("d14input.txt", "r") as f:
    ex_input = f.readlines()

ilst = [x.strip() for x in ex_input]
#ilst = [x for x in ex_input.split("\n")]

def get_value(mem_str):
    #ival = int(mem_str.split("=")[-1])
    #ival_bin = str(bin(ival))[2:]
    #breakpoint()
    ival_bin = str(bin(int(mem_str.split("[")[-1].split("]")[0])))[2:]
    value = ("0" * (36 - len(ival_bin))) + ival_bin
    return value

def get_mask(mask_str):
    return mask_str.split("=")[-1].strip()


def get_result(mask, value):
    res = ""
    for mv, rv in zip(mask, value):
        if mv == "1":
            res = res + "1"
        elif mv == "X":
            res = res + "X"
        elif mv == "0" and rv == "1":
            res = res + "1" 
        else:
            res = res + "0"
    #print(f"{value=}\n{mask=}\n{res=}")
    n_res = genCombinations(res)
    return n_res

def binStrToInt(binStr):
    num = 0
    for v in binStr:
        num = num * 2
        num = num + int(v)
    return num

def genCombinations(result):
    values = []
    x_pos = [x for x in range(len(result)) if result[x] == "X"]
    #combs = tuple(set(combinations_with_replacement((1, 0, 1, 0), len(x_pos))))
    combs = set(mask for mask in product(*[[0, 1]] * len(x_pos)))
    for vals in combs:
        n_res = list(result)
        for val, idx in zip(vals, x_pos):
            n_res[idx] = str(val)
        n_res = "".join(n_res)
        values.append(binStrToInt(n_res))
    return values

res_dict = {}
mask = get_mask(ilst[0])
for inst in ilst[1:]:
    inst_type = inst[:3]

    if inst_type == "mas":
        mask = get_mask(inst)
    else: # é "mem"
        mpl = get_result(mask, get_value(inst))
        val = int(inst.split("=")[-1])

        for mp in mpl:
            res_dict[mp] = val

#print(res_dict.items())
print(sum(res_dict.values()))
