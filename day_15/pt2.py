import collections
# takes a lot of time to get the result

input_data = [int(x)  for x in "0,13,1,8,6,15".split(",")]

prev_seen = collections.defaultdict(list)

for i, v in enumerate(input_data):
    prev_seen[v].append(i)


# minha 
"""
i = len(input_data)
last_n = input_data[-1]
while i < 30_000_000:
    if len(prev_seen[last_n]) == 1:
        last_n = 0
    else:
        last_n = prev_seen[last_n][-1] - prev_seen[last_n][-2]
    prev_seen[last_n].append(i)
    i += 1
print(last_n)
"""
it = 30_000_000
for t in range(it):
    if t < len(input_data):
        n = input_data[t]
    elif len(prev_seen[n]) == 1:
        n = 0
    else:
        n = prev_seen[n][-1] - prev_seen[n][-2]
    prev_seen[n].append(t)
print(n)
