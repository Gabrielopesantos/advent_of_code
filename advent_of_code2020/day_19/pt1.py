from collections import defaultdict

ex_input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

def parse_rules(raw_rls):
    rls_dict = defaultdict(list)

    for r in raw_rls.split("\n"):
        k, v = r.split(": ")
        for s in v.split(" | "):
            rls_dict[k].append(s.split(" "))

    return rls_dict

def check_if_obeys(msg):
    print(msg)

    


if __name__ == "__main__":

    with open("d19input.txt", "r") as f:
        rrules, rstrings = f.read().split("\n\n")

    msgs = [list(x) for x in rstrings.strip().split("\n")]
    tot_msgs = len(msgs)

    rules = parse_rules(rrules)

    print(rules["0"])
    for msg in msgs:
        check_if_obeys(msg)
        break
