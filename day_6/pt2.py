groups_list = []

with open("input.txt", "r") as f:
    input_data = [x.strip() for  x in f.readlines()]

input_data.append("")

temp_list = []
n_members = 0
for l in input_data:
    if l != "":
        temp_list.append(l)
        n_members += 1
    else:
        groups_list.append((n_members, temp_list))
        n_members = 0
        temp_list = []
        #temp_list.clear()

cnt = 0

for n_members, grp in groups_list:
    # concat list elements into str
    cnter_dict = dict()
    grp_str = "".join(grp)
    
    for c in grp_str:
        if c in cnter_dict.keys():
            cnter_dict[c] = cnter_dict[c] + 1
        else:
            cnter_dict[c] = 1

    #cnt += sum([1 for x in cnter_dict.keys() if cnter_dict[c] == n_members])
    cnt += sum([1 if cnter_dict[x] == n_members else 0 for x in cnter_dict.keys()])

print(cnt)
