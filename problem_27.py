from math import sqrt
from time import time

MAX_A = 1000
MAX_B = 1000


def is_prime(n):
    if n <= 0:
        return False
    for i in range(3, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    prod = 0
    max_seq = 0
    couple = (0, 0)
    t = time()
    b_list = []
    for i in range(1, MAX_B):
        if is_prime(i):
            b_list.append(i)
    for a in range(-1*MAX_A+1, MAX_A):
        for b in b_list:
            n = 0
            while is_prime(n*n + a*n + b):
                n += 1
            if n > max_seq:
                prod = a*b
                max_seq = n
                couple = (a, b)
    print 'Couple:', couple, 'Max sequence:', max_seq, 'Product:', prod, 'Time:', time() - t
