with open("input.txt", "r") as f:
    l = [int(x.strip()) for x in f.readlines()]

def get_differences(lst):
    diffs_dict = {}
    lst.append(0)
    lst.append(max(lst) + 3)
    #lst = list(set(lst))
    lst.sort()
    #print(lst)
    for i, pos in enumerate(lst):
        entered = False
        diff_pos = 1
        while True:
            if entered or i + diff_pos > len(lst) - 1:
                break
            else:
                if (diff := lst[i + diff_pos] - lst[i]) > 3:
                    break
                else:
                    #print(lst[i], lst[i + diff_pos], lst[i + diff_pos] - lst[i])
                    if diff in diffs_dict.keys():
                        diffs_dict[diff] = diffs_dict[diff] + 1
                    else:
                        diffs_dict[diff] = 1
                    entered = True
                    diff_pos += 1
    
    #print(diffs_dict)
    print(diffs_dict[3] * diffs_dict[1])

get_differences(l)
