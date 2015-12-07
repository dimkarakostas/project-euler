l = []
i = 10
while len(str(i))*(9**5) > i:
    sm = 0
    for d in str(i):
        sm += int(d)**5
    if sm == i:
        l.append(i)
    i += 1
print l, sum(l)
