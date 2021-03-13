import time
from collections import deque
from itertools import islice

def play_game(p1, p2):
    all_rounds = {1:set(), 2:set()}
    while len(p1) != 0 and len(p2) != 0:
        t_p1 = tuple(p1)
        t_p2 = tuple(p2)
        if t_p1 in all_rounds[1] and t_p2 in all_rounds[2]:
            p2.clear()
            break
        else:
            all_rounds[1].add(t_p1)
            all_rounds[2].add(t_p2)

        c_p1 = p1.popleft()
        c_p2 = p2.popleft()

        if len(p1) >= c_p1 and len(p2) >= c_p2:
            dp1, dp2 = play_game(deque(islice(p1, c_p1)), deque(islice(p2, c_p2)))
            sp1, sp2 = [sum(val * mult for mult, val in enumerate(reversed(dp),\
                    start=1)) for dp in [dp1, dp2]]
            if sp1 > sp2:
                r_winner = 1
            else:
                r_winner = 2
        elif c_p1 > c_p2:
            r_winner = 1 
        else:
            r_winner = 2

        if r_winner == 1:
            p1.extend([c_p1, c_p2])
        else:
            p2.extend([c_p2, c_p1])

    return p1, p2

def main():
    time_start = time.perf_counter()
    with open("d22input.txt", "r") as f:
        players = [line.strip() for line in f.read().strip().split("\n\n")]
    
    p1 = deque(int(i) for i in players[0].split("\n")[1:])
    p2 = deque(int(i) for i in players[-1].split("\n")[1:])
    
    deck1, deck2 = play_game(p1, p2)
    highest_s = max([sum(val * mult for mult, val in enumerate(reversed(dp),\
                    start=1)) for dp in [deck1, deck2]])
    print(highest_s)
    print(f"{time.perf_counter() - time_start}")
        
if __name__ == "__main__":
    main()
