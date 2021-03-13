with open("d22input.txt", "r") as f:
    p1, p2 = [list(map(int, x.strip().split("\n")[1:]))\
           for x in f.read().split("\n\n")]

    #p1, p2 = [9, 2, 6, 3, 1], [5, 8, 4, 7, 10]
    
def play_game(p1, p2, history, sub=False):
    i = 0
    while True:
        #print(history, [True if p1 == p1h and p2 == p2h else False for p1h, p2h in\
        #        history[:-1]], p1, p2, sep="\n")
        if len(p1) == 0 or len(p2) == 0:
            return p1, p2
        elif any([True if p1 == p1h and p2 == p2h else False for p1h, p2h in\
                history[:-1]]):
            p2.clear()
            return p1, p2
    
        p1c = p1.pop(0)
        p2c = p2.pop(0)

        if p2c <= len(p2) and p1c <= len(p1): 
            p1_s, p2_s = play_game(p1[:p1c].copy(), p2[:p2c].copy(), [], sub=True)
            p1_s, p2_s = [sum([val * mult for mult, val in zip(range(1, len(p)+1),\
                p[::-1])]) for p in [p1_s, p2_s]]
            
            if p1_s > p2_s:
                p1.extend([p1c, p2c])
            else:
                p2.extend([p2c, p1c])
        else:
            if p1c > p2c:
                p1.extend([p1c, p2c])
            else:
                p2.extend([p2c, p1c])
        history.append([p1.copy(), p2.copy()])
        i+= 1

s1, s2 = play_game(p1, p2, [], False)
print(s1, s2)
highest_score = max(sum([val * mult for mult, val in zip(range(1, len(p)+1),\
        p[::-1])]) for p in [s1, s2])
print(highest_score)
