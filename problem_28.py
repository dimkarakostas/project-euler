k = 1
s = 0

for l in range(0, 1002, 2):
    for i in range(0, 4):
        s += k + l*(l - 1) + l*i
print s-3
