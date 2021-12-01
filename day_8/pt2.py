def get_data():
    with open("input.txt", "r") as f:
        l = [[x.split()[0], int((x.split()[-1]).strip()), 0] for x in f.readlines()]
    return l

l = get_data()
    
tmp = [[i, x[0]] for i, x in enumerate(l) if x[0] in ["jmp", "nop"]]

pos = 0
accumulator = 0

def exec_instruction(c_pos):
    op, arg, cnts = l[c_pos]
    global accumulator, pos

    
    if op == "acc":
        accumulator += arg
        pos += 1
    elif op == "jmp":
        pos += arg
    elif op == "nop":
        pos += 1

    l[c_pos][-1] += 1

for case_i, case_n in tmp:
    
    if case_n == "jmp":
        l[case_i][0] = "nop"
    else:
        l[case_i][0] = "jmp"

    while True:
        if pos > len(l) -1:
            print(accumulator)
            #print(case_i, case_n, accumulator)
            break
        
        if l[pos][-1] > 1:
            break
        
        exec_instruction(pos)

    l = get_data()
    pos = accumulator = 0
