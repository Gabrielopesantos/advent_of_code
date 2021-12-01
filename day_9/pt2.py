with open("input.txt", "r") as f:
    l = [int(x.strip()) for x in f.readlines()]

def get_we(lst, prev_nmb = 31161678):
    start = 0
    end = 0

    while True:
        curr_sum = sum(lst[start:end])

        if curr_sum == prev_nmb:
            #print(start, end)
            #print(l[start], l[end],sum(l[start:end]))
            print(min(l[start:end]) + max(l[start:end]))
            break
        elif curr_sum < prev_nmb:
            end += 1
        elif curr_sum > prev_nmb:
            start += 1

get_we(l)
