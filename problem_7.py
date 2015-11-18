from time import time
from math import sqrt


def is_prime(n):
    for i in range(3, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

cnt = 0
i = 1
ar = [2]
t = time()
print t
while len(ar) < 10001:
    i += 2
    if is_prime(i):
        ar.append(i)
print time()
print i, time() - t
