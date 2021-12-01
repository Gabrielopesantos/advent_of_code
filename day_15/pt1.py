input_data = [int(x)  for x in "0,13,1,8,6,15".split(",")]
#input_data = [0, 3, 6]

n_dict = {input_data[x]: [x +1] for x in range(len(input_data))}
#print(n_dict)
i = 0
while i < 2030:
    #if i == 10:
    #    break
    cn = input_data[-1]
    if len(n_dict[cn]) == 1:
        input_data.append(0)
        
        n_dict[0] = n_dict[0] + [len(input_data)]
    else:
        n = n_dict[cn][-1] - n_dict[cn][-2]
        input_data.append(n)
        if n in n_dict.keys():
            n_dict[n] = n_dict[n] + [len(input_data)]
        else:
            n_dict[n] = [len(input_data)]
    i += 1
    #print(i, n_dict, input_data, sep="\n")
#print(input_data)
print(input_data[2019])
