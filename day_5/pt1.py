def get_pos(l, bot, top, n_small, n_big):
    for c in l:
        tmp_num = int((n_small + n_big) / 2)
        if c == bot: ## F = Lower half
            n_big = tmp_num 
        else: ## B = upper half
            tmp_num += 1
            n_small = tmp_num
            
        #print(c, n_small, n_big)
    #print(tmp_num)
    return tmp_num

with open("input.txt", "r") as f:
    l =  [x.strip() for x in f.readlines()]

highest = 0
for str_pos in l:
    row = get_pos(str_pos[:-3], "F", "B", 0, 127)
    seat = get_pos(str_pos[-3:], "L", "R", 0, 7)
    #print(f"Code {str_pos} | row {row} | seat {seat} | mul {(row * 8) + seat}")
    if (tmp := (row * 8) + seat) > highest:
        highest = tmp
    
print(highest)

## Caso 1
# ROW
"""
t = "FBFBBFF"
bot = "F"
top = "B"
n_small = 0
n_big = 127
get_pos(t, bot, top, n_small, n_big)

# POS na row

t = "RLR"
bot = "L"
top = "R"
n_small = 0
n_big = 7
get_pos(t, bot, top, n_small, n_big)
"""
