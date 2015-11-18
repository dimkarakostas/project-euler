def prime_factors(n):
    '''
    Returns a list of all prime factors of n in ascending order.
    '''
    factors = []
    d = 2
    while n > 1:
        if n % d == 0:
            factors.append(d)
            n /= d
        else:
            d += 1
    return factors


n = 600851475143
factors = prime_factors(n)
print("Biggest prime factor of %d is %d" % (n, factors[-1]))
