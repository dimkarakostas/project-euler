import numpy as np
from math import sqrt


def get_primes_below(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k = 3*i+1 | 1
            sieve[((k*k)/3)::2*k] = False
            sieve[(k*k+4*k-2*k*(i & 1))/3::2*k] = False
    return np.r_[2, 3, ((3*np.nonzero(sieve)[0]+1) | 1)]


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
