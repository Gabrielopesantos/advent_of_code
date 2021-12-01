with open("input.txt", "r") as f:
    l = [int(x.strip()) for x in f.readlines()]


def get_st_fake_number(preamble, lst):
    curr_pos = preamble

    while True:
        sums = [x + y for x in lst[curr_pos-preamble:curr_pos] \
                for y in lst[curr_pos-preamble:curr_pos] if x != y]
        
        if (tmp := lst[curr_pos]) not in sums:
            print(tmp)
            break

        curr_pos += 1

get_st_fake_number(25, l)
