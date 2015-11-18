from math import sqrt

LIM = 2000000


def is_prime(n):
    for i in range(3, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

s = 2
i = 1
while i < LIM:
    i += 2
    if is_prime(i):
        s += i
print s
