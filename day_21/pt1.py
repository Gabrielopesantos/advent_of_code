from collections import defaultdict

def parse_input(lines):
    return [[[ing.strip() for ing in x.split("(")[0].split()],\
            [x.strip() for x in x[:-2].split("(contains")[-1].split(",")]]\
            for x in lines]


example_input = ["mxmxvkd kfcds sqjhc nhms (contains dairy, fish)\n",
"trh fvjkl sbzzf mxmxvkd (contains dairy)\n",
"sqjhc fvjkl (contains soy)\n",
"sqjhc mxmxvkd sbzzf (contains fish)\n"]

with open("d21input.txt", "r") as f:
    foods = parse_input(f.readlines()) 

#foods = parse_input(example_input)

all_ingredients = []
d = defaultdict(list)
for ingredients, allergens in foods:
    all_ingredients.extend(ingredients)
    for allergen in allergens:
        d[allergen].append(set(ingredients))

#lst = [(k, [(ing, v.count(ing)) for ing in set(v)]) for k, v in d.items()]

d = {k: set.intersection(*v) for k, v in d.items()}

#print(sum(all_ingredients.count(ing) for ing in\
#        set(all_ingredients).difference(set.union(*d.values()))))

confirmed = {}

while len(confirmed)  < len(d):
    for allergen in d:
        nset = d[allergen].difference(confirmed.values())

        if len(nset) == 1:
            confirmed[allergen] = nset.pop()

        d[allergen] = nset

print(",".join(v for k, v in sorted(confirmed.items(), key=lambda x: x[0])))
