from math import pow

n = int(pow(2, 1000))
out = 0
for i in str(n):
    out += int(i)
print out
