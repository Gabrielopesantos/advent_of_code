from collections import deque

ex_input = "389125467"
p_input = "871369452"

def gen_inflst(inp):
    i = 0
    while True:
        if i == len(inp) - 1:
            i = 0
        yield inp[i]
        i += 1

def compute_pt1(str_input, moves=100):
    str_input = list(map(int, str_input))
    c_pos_idx = 0
    for ii in range(moves):
        if c_pos_idx > len(str_input) - 1:
            c_pos_idx = c_pos_idx % len(str_input)
        t_pos = c_pos_idx + 1 
        
        c_pos_val = str_input[c_pos_idx]

        popped_elems = []
        for i in range(1, 5, 1):
            if c_pos_idx + i > len(str_input) - 1:
                idx = (c_pos_idx + i) % len(str_input)
                if i == 4:
                    nxt_first = str_input[idx]
                    break
                popped_elems.append(str_input[idx])
            else:
                if i == 4:
                    nxt_first = str_input[c_pos_idx+i]
                    break
                popped_elems.append(str_input[c_pos_idx+i])

        str_input = [x for x in str_input if x not in popped_elems]

        if c_pos_val == min(str_input):
            val = max(set(str_input).difference(popped_elems))
        else:
            val = sorted([x for x in str_input if x < c_pos_val],\
                    key=lambda x: x)[-1]


        str_input = str_input[:str_input.index(val)+1] + popped_elems + \
                str_input[str_input.index(val)+1:]
        
        #str_input = str_input[str_input.index(nxt_first):] +\
        #        str_input[:str_input.index(nxt_first)] 

        c_pos_idx += 1
        diff = c_pos_idx - str_input.index(nxt_first)
        if diff > 0:
            for _ in range(abs(diff)):
                str_input = [str_input[-1]] + str_input[:-1]
        elif diff < 0:
            for _ in range(abs(diff)):
                str_input = str_input[1:] + [str_input[0]]
        #print(ii+2, str_input)
    return str_input    


str_input = compute_pt1(p_input, 100)
print(str_input)
