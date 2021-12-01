import re

with open("input.txt", "r") as f:
    lines = f.read().split("\n\n")
    passports =  [re.sub("[\n]"," ", line) for line in lines]
    
    cnt = 0
    for passp in passports:
        passp_s = passp.split()

        cid = sum([0 if x.split(":")[0] == "cid" else 1 for x in passp_s])

        if len(passp_s) == 8:
            cnt += 1
        elif len(passp_s) == 7 and cid == 7:
            cnt += 1
        
    print(cnt)
