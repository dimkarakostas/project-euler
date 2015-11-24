from math import sqrt
from time import time


def is_prime(n):
    for i in range(3, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def div_sum(n):
    if is_prime(n):
        return 1
    s = 1
    forward = 2
    backward = n
    while forward < backward:
        if n % forward == 0:
            backward = n / forward
            s += forward + backward
        forward += 1
    if forward-1 == backward:
        s -= backward
    return s


t = time()
agg = []
for i in range(4, 10000):
    di = div_sum(i)
    if di < i:
        continue
    if i == div_sum(di) and i != di:
        agg.append(i)
        agg.append(di)

print 'Sum:', sum(agg), 'Time:', time() - t
