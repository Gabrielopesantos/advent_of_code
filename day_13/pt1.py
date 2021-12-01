with open("input.txt", "r") as f:
    n, lst = [x.strip() for x in f.readlines()]

lst = [int(x) for x in lst.split(",") if x != "x"]
n = int(n)
lst.sort()

#print(n, lst)
#highests = []

#for val in lst:
#    tsum = 0
#    while tsum < int(n):
#        tsum += val
#    highests.append(tsum)
#
#bus = lst[highests.index(min(highests))]
#print((min(highests) - int(n)) * bus)

min_time = ((n //  lst[0] + 1) * lst[0])
bus_id = 0

for i, bus in enumerate(lst[1:]):
    time = ((n //  bus + 1) * bus)
    if time < min_time:
        min_time = time
        bus_id = i

print((min_time - n) * lst[i])
