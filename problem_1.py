sum = 0
for i in xrange(1000):
    sum += i if ((i % 3 == 0 and i > 2) or (i % 5 == 0 and i > 4)) else 0
print sum
