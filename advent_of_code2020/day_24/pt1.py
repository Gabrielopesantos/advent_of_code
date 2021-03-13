from collections import Counter

moves = ["e", "se", "sw" , "w", "nw", "ne"]
chng_color = {"white":"black", "black":"white"}

def parse_input(tile_moves):
    
    mvs_lst = []
    for i in range(len(tile_moves)):
        if tile_moves[i] in moves:
            mvs_lst.append(tile_moves[i])
        else:
            mvs_lst.append(tile_moves[i:i+2])

    # linha desnecessária
    mvs_lst = [mvs_lst[0]] + [mvs_lst[i] for i in range(1, len(mvs_lst)) if\
            mvs_lst[i-1] not in ["se", "ne", "sw", "nw"]]

    return mvs_lst


def compute(mvs_lsts):

    flips_dict = {}
    for mvs in mvs_lsts:
        init_pos = [0, 0] 

        for mv in mvs:
            if mv == "e":
                init_pos = [init_pos[0] + 2, init_pos[-1]]
            elif mv == "w":
                init_pos = [init_pos[0] - 2, init_pos[-1]]
            elif mv == "ne":
                init_pos = [init_pos[0] + 1, init_pos[-1] + 1]
            elif mv == "nw":
                init_pos = [init_pos[0] - 1, init_pos[-1] + 1]
            elif mv == "se":
                init_pos = [init_pos[0] + 1, init_pos[-1] - 1]
            elif mv == "sw":
                init_pos = [init_pos[0] - 1, init_pos[-1] - 1]

        if tuple(init_pos) in flips_dict:
            flips_dict[tuple(init_pos)] = chng_color[flips_dict[tuple(init_pos)]]
        else:
            flips_dict[tuple(init_pos)] = "black"
    return flips_dict

def compute_pt2(dct, days=100):
    adjacents = [(2, 0), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for i in range(days):
        cnter = Counter()
        for (hex_x, hex_y), hex_color in dct.items():
            for adj_x, adj_y in adjacents:
                adj_tpl = tuple([hex_x + adj_x, hex_y + adj_y])
                if hex_color == "black":
                    cnter[adj_tpl] += 1
                else:
                    cnter[adj_tpl] += 0

        n_dict = {}
        for (x, y), c in cnter.items():
            tpl = tuple([x, y])
            if tpl in dct.keys():
                if dct[tpl] == "black":
                    if c == 0 or c > 2:
                        n_dict[tpl] = "white"
                    else:
                        n_dict[tpl] = "black"
                else:
                    if c == 2:
                        n_dict[tpl] = "black"
                    else:
                        n_dict[tpl] = "white"
            else: 
                if c == 2:
                    n_dict[tpl] = "black"
                else:
                    n_dict[tpl] = "white"

        dct = n_dict
        print(i+1, sum([1 if v == "black" else 0 for v in dct.values()]))

with open("d24input.txt", "r") as f:
    input_ = [x.strip() for x in f.readlines()]


# PT1

mvs = [parse_input(lst) for lst in input_]
dct = compute(mvs)
print(sum([1 if v == "black" else 0 for v in dct.values()]))

# PT 22 
compute_pt2(dct)

