MAX_A = 100
MAX_B = 100

s = set()
for a in range(2, MAX_A+1):
    for b in range(2, MAX_B+1):
        s.add(a**b)
print len(s)
