with open("input.txt", "r") as f:
    l = [[x.split()[0], int((x.split()[-1]).strip()), 0] for x in f.readlines()]

accumulator = 0
pos = 0

def exec_instruction(inst_pos):
    global accumulator, pos
    op, arg, cnts = l[inst_pos]
    check = True 

    if cnts > 1:
        check = False
    else:
        if op == "acc":
            accumulator += arg
            pos += 1
        elif op == "jmp":
            pos += arg
        elif op == "nop":
            pos += 1 
    
        l[pos][-1] += 1
    return check


while True:
    if not exec_instruction(pos):
        break

print(accumulator)
