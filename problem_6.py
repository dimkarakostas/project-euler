a = b = 0

for i in range(1, 101):
    a += i*i
    b += i

b = b*b
print a, b, b-a
