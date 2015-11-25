x = y = 1
index = 2
while len(str(x)) < 1000:
    index += 1
    z = x
    x += y
    y = z
print index
