import math


class PrimeFactorization():
    '''
    Solution using prime factorization.
    '''
    def __init__(self, field):
        self.field = field
        return

    def get_prime_factors(self, n):
        '''
        Returns a dict of prime factors as keys and the powers as values.
        '''
        factors = {}
        d = 2
        while n > 1:
            if n % d == 0:
                if d in factors:
                    factors[d] += 1
                else:
                    factors[d] = 1
                n /= d
            else:
                d += 1
        return factors

    def factorize(self):
        factors = {}
        sum = 1
        for i in self.field:
            factors_i = self.get_prime_factors(i)
            for key, value in factors_i.items():
                if key not in factors or factors[key] < value:
                    factors[key] = value
        for key, value in factors.items():
            sum *= math.pow(key, value)
        return int(sum)

if __name__ == "__main__":
    field = []
    for i in xrange(20, 1, -1):
        field.append(i)
    pf = PrimeFactorization(field)
    print pf.factorize()
