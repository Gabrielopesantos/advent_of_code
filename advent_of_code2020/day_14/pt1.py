ex_input = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0\n"

with open("d14input.txt", "r") as f:
    ex_input = f.readlines()

ilst = [x.strip() for x in ex_input]

#breakpoint()

def get_value(mem_str):
    #print(mem_str)
    ival = int(mem_str.split("=")[-1])
    ival_bin = str(bin(ival))[2:]
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
            res = res + rv
        else:
            res = res + "0" 
    #print(f"{value=}\n{mask=}\n{res=}")
    return res

def binStrToInt(binStr):
    num = 0
    for v in binStr:
        num = num * 2
        num = num + int(v)
    return num

res_dict = {}
mask = get_mask(ilst[0])
for inst in ilst[1:]:
    inst_type = inst[:3]

    if inst_type == "mas":
        mask = get_mask(inst)
    else: # é "mem"
        decimal = binStrToInt(get_result(mask, get_value(inst)))

        #if (val_key := int(inst.split("=")[-1])) in res_dict.keys():
        #    res_dict[val_key] = decimal
        #else:
        
        #breakpoint()
        mem_pos = int(inst.split("[")[-1].split("]")[0])
        #print(mem_pos)
        res_dict[mem_pos] = decimal


#print(res_dict)
print(sum(res_dict.values()))
