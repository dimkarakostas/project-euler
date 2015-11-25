from math import sqrt
from time import time


abundant = non_sum_ab = set()


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
    while forward < backward and forward < int(sqrt(n)):
        if n % forward == 0:
            backward = n / forward
            s += forward + backward
        forward += 1
    if forward-1 == backward:
        s -= backward
    return s


def check_abundancy(n):
    for ab in abundant:
        if n-ab in abundant:
            return
    non_sum_ab.add(n)


t = time()
for i in range(1, 28123):
    if i < div_sum(i):
        abundant.add(i)
    check_abundancy(i)
print sum(non_sum_ab), time() - t
