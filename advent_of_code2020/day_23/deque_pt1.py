from collections import deque

ex_input = "389125467"
p_input = "871369452"

def gen_output(str_input, moves=100):
    cups = deque([int(n) for n in list(str_input.strip())])
    max_ = len(cups)

    for ii in range(moves):
        c_cup = cups[0]
        cups.rotate(-1)
        popped_cups = [cups.popleft() for _ in range(3)]

        c_label = c_cup - 1
        if c_label == 0:
            c_label = max_
        while c_label in popped_cups:
            c_label = (c_label - 1)
            if c_label == 0:
                c_label = max_
        
        idx = cups.index(c_label)
        cups.rotate(-1 * idx - 1)
        cups.extend(popped_cups)
        cups.rotate(idx + 3 + 1)

    cups.rotate(-cups.index(1))
    cups.popleft()
    return cups

str_input = gen_output(p_input, 100)
print(str_input)
