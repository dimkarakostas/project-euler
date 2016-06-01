from time import time
from itertools import permutations
from math import sqrt

DIGITS = '123456789'


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def prime_pandigitals(n):
    pp = []
    for p in permutations(str(DIGITS)[:n]):
        perm = int(''.join(p))
        if is_prime(perm):
            pp.append(perm)
            break
    return pp


def main():
    for digit_count in range(7, 0, -1):
        perms = [int(''.join(p)) for p in permutations(str(DIGITS)[:digit_count])]
        for perm in sorted(perms, reverse=True):
            if is_prime(perm):
                print perm
                return

if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
