groups_list = []

with open("input.txt", "r") as f:
    input_data = [x.strip() for  x in f.readlines()]

input_data.append("")

temp_list = []
for l in input_data:
    if l != "":
        temp_list.append(l)
    else:
        groups_list.append(temp_list)
        temp_list = []
        #temp_list.clear()

cnt = 0

for grp in groups_list:
    # concat list elements into str
     cnt += len(set("".join(grp)))

print(cnt)
