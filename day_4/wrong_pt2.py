import re

hcl_check = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", \
                "d", "e", "f"]

def check_rules(fields_dict):

    for field, val in fields_dict.items():
        if field == "byr" and int(val) >= 1920 and int(val) <= 2002 and \
                len(str(val)) == 4:
            pass
        elif field == "iyr" and 2010 <= int(val) <= 2020 and len(str(val)) == 4:   
            pass
        elif field == "eyr"  and 2020 <= int(val) <= 2030 and len(str(val)) == 4: 
            pass
        elif field == "hgt":
            val = str(val)
            if val[-2:] == "cm" and 150 <= int(val[:-2]) <= 193:
                pass
            elif val[-2:] == "in" and 59 <= int(val[:-2]) <= 76:
                pass
        elif field == "hcl" and val[0] == "#" and len(str(val[1:])) == 6 and \
                all([True if x in hcl_check else False for x in val[1:]]):
            pass
        elif field == "ecl" and val in ["amb", "blu", "brn", "gry", "grn",
                "hzl", "oth"]:
            pass
        elif field == "pid" and len(str(val)) == 9:
            pass
        else:
            #print("FALSE", fields_dict)
            return False
    
    #print("TRUE", fields_dict)
    return True

with open("day_4_input.txt", "r") as f:
    lines = f.read().split("\n\n")
    passports =  [re.sub("[\n]"," ", line) for line in lines]
    
    cnt = 0
    for i, passp in enumerate(passports):
        fields_dict = {x.split(":")[0]:x.split(":")[-1] for x in passp.split(" ")}
    
        if '' in fields_dict:
            del fields_dict['']
        
        if 'cid' in fields_dict:
            del fields_dict['cid']

        nFields = len(fields_dict.keys())
        hasCID = True if fields_dict.get("cid") else False
        #print(nFields, hasCID, fields_dict, end="\n")
       
        if nFields == 8 or nFields == 7 and hasCID == False:
            if check_rules(fields_dict):
                cnt += 1
                print("TRUE", fields_dict)
            else:
                print("FALSE", fields_dict)

    print(cnt)
