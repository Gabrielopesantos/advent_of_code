from collections import defaultdict

with open("d20input.txt", "r") as f:
    imgs = {int(i.split(" ")[-1].split(":")[0]):i.split(":")[-1].strip() for i in\
            f.read().split("\n\n")}

def generate_edges(tile):
    edges = []
    edges.append(tile.split("\n")[0])
    edges.append(tile.split("\n")[-1])
    edges.append("".join([x[0] for x in tile.split("\n")]))
    edges.append("".join([x[-1] for x in tile.split("\n")]))

    tot_edges = [x[::-1] for x in edges] + edges
    
    return tot_edges

tils = []
for tid1, til1 in imgs.items():
    t1_edges = set(generate_edges(til1))
    for tid2, til2 in imgs.items():
        if tid1 == tid2:
            continue
        else:
            t2_edges = set(generate_edges(til2))
            for e in t2_edges:
                if e in t1_edges:
                    t1_edges.discard(e)
    if len(t1_edges) == 4:
        tils.append(tid1)

mult = 1
for v in tils:
    mult *= v
print(mult)
