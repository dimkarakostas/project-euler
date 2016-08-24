from time import time
from problem_35 import is_prime


def main():
    primes = [2, 3]
    consecutives = []
    number_of_consecutives = 4
    index = 3

    while len(consecutives) < number_of_consecutives:
        index += 1

        if is_prime(index):
            primes.append(index)
            consecutives = []
            continue

        prime_factors = set()
        factored = index
        for prime in primes:
            while factored % prime == 0 and factored and len(prime_factors) < number_of_consecutives + 1:
                prime_factors.add(prime)
                factored /= prime
            if not factored or len(prime_factors) > number_of_consecutives - 1:
                break

        if len(prime_factors) == number_of_consecutives:
            consecutives.append(index)
        else:
            consecutives = []

    print consecutives


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
