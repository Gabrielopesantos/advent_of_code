ex_inp = "5764801,17807724"
puzzle_inp = "15335876,15086442"

def compute_pt1(public_keys):
    keys = list(map(int, public_keys.split(",")))
    loop_sizes = []
    encryption_keys = []
    for k in keys:
        init = 1
        loop_size = 0
        while init != k:
            init *= 7
            init = init % 20201227
            loop_size += 1

        loop_sizes.append(loop_size)
        
    for pk, ls in zip(reversed(keys), loop_sizes):
        enc_k = 1

        for _ in range(ls):
            enc_k *= pk
            enc_k %= 20201227
        encryption_keys.append(enc_k)
    
    if encryption_keys[0] == encryption_keys[1]:
        print(encryption_keys[0])
    else:
        print("ERRO")

compute_pt1(puzzle_inp)
