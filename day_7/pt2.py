bags_dict = {}

with open("input.txt", "r") as f:

    input_data = f.readlines()

for id_str in input_data:
    b_name, r = id_str[:-2].split("bags contain")
    b_name = b_name.strip()
    r = [(x[1], x[2:-4].strip()) for x in r.split(",")]
    #r = [x[2:-4].strip() for x in r.split(",")]
    if "no other bags" in id_str:
        bags_dict[b_name] = []
    else:
        bags_dict[b_name] = r
    #bags.append((b_name, r))


cnter = 0

bags = [bags_dict["shiny gold"]]
while True:
    #print(bags)
    if not bags:
        break
    tmp_bags = []
    
    #print(cnter, bags)
    for bag in bags:
        for b_number, b_name in bag:
            #print(cnter)
            cnter += int(b_number)
            
            if bags_dict[b_name]: 
                #print("entrei e o valor é", bags_dict[b_name])
                [tmp_bags.append(bags_dict[b_name]) for _ in range(int(b_number))]
     
    bags = tmp_bags
    #print(bags, cnter)
    
print(cnter)
