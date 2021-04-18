def get_pos(l, bot, top, n_small, n_big):
    for c in l:
        tmp_num = int((n_small + n_big) / 2)
        if c == bot: ## F = Lower half
            n_big = tmp_num 
        else: ## B = upper half
            tmp_num += 1
            n_small = tmp_num
            
    return tmp_num

with open("input.txt", "r") as f:
    l =  [x.strip() for x in f.readlines()]

list_seats = []

for str_pos in l:
    row = get_pos(str_pos[:-3], "F", "B", 0, 127)
    seat = get_pos(str_pos[-3:], "L", "R", 0, 7)
    
    list_seats.append(int((row * 8) + seat))

all_seat_ids = [int((x * 8) + y) for x in range(0, 128) for y in range(0, 8)]
flrsids = [x * 8 + y for x in [0, 1, 2, 3, 124, 125, 126, 127] for y in range(0,8)]

missing_seats = []

for sid in all_seat_ids:
    if sid not in list_seats:
        missing_seats.append(sid)

# breakpoint()