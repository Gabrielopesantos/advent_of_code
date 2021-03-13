with open("input.txt", "r") as f:
    l = [int(x.strip()) for x in f.readlines()]

l.append(0)
l.append(max(l)+3)
l.sort()


def combs(s):
    if s == 0:
        return 1
    elif s== 1:
        return 1
    elif s == 2:
        return 2
    else:
        return combs(s-1) + combs(s-2) + combs(s-3)


mult = 1
streak = 0
prev = 0
diff = 0
mult1 = 1

for val in l[1:]:
    if val == prev + 1 or val == prev:
        streak += 1
    else:
        #print(streak)
        mult *= combs(streak)
        streak = 0

    prev = val


# O (n)
for i in range(len(l)):
    streak = 0
    acc_diff = 0
    prev_diff = 0
    # O (log n)
    for j in range(i+1, len(l)):
        diff = l[j] - l[i]
        acc_diff  += diff - prev_diff

        if acc_diff >= 3:
            mult1 *= combs(streak)
            break
        else:
            streak += 1
            prev_diff = diff

print(f"{mult=}")
