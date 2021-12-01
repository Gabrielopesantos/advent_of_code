bags = []
with open("input.txt", "r") as f:
    input_data = f.readlines()

for id_str in input_data:
    b_name, r = id_str[:-2].split("bags contain")
    b_name = b_name.strip()
    #r = [(x[1], x[2:-4].strip()) for x in r.split(",")]
    r = [x[2:-4].strip() for x in r.split(",")]

    bags.append((b_name, r))

cnter = []
hasColors = ["shiny gold"]
while True:
    if not hasColors:
        break
    tmp_hasColors = []

    for bag_name, bag_contains in bags:
        for color in hasColors:
            if color in bag_contains:
                tmp_hasColors.append(bag_name)
    
    hasColors = tmp_hasColors
    cnter.append(tmp_hasColors)

unique_colors = len(set([x for y in cnter for x in y]))
print(unique_colors)

# 172
