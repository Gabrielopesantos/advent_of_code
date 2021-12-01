import re

data_patterns = {
        "byr" : re.compile(r"^[0-9]{4}$"),
        "iyr" : re.compile(r"^[0-9]{4}$"),
        "eyr" : re.compile(r"^[0-9]{4}$"), 
        "hgt" : re.compile(r"^[0-9]+(cm|in)$"), 
        "hcl" : re.compile(r"^#[0-9a-f]{6}$"), 
        "ecl" : re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"), 
        "pid" : re.compile(r"^[0-9]{9}$")
        }

data_checks = {
        "byr" : (lambda x: (1920 <= int(x) <= 2002)),
        "iyr" : (lambda x: (2010 <= int(x) <= 2020)),
        "eyr" : (lambda x: (2020 <= int(x) <= 2030)),
        "hgt" : (lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or \
                (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)),
        "hcl" : (lambda x: True),
        "ecl" : (lambda x: True),
        "pid" : (lambda x: True)
        }

cnt = 0
with open("input.txt", "r") as f:
    passports = [x for x in f.read().split("\n\n")]
    

for p in passports:
    #p = re.sub("\n", " ", p)

    fields_dict = {x.split(":")[0]:x.split(":")[-1] for x in p.split()}

    if fields_dict.get("cid"):
        del fields_dict["cid"]
    
    if len(fields_dict.keys()) == 7:

        check = True
        for f, v in fields_dict.items():
            if data_checks[f](v) and data_patterns[f].match(v):
                continue
            else:
                check = False
                break
        if check:    
            #print(fields_dict)
            cnt += 1
    else:
        pass
print(cnt)
