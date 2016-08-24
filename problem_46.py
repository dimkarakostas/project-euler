from time import time
from math import sqrt
from problem_35 import is_prime


def main():
    primes = set()
    index = 1
    found_composite = 0

    while not found_composite:
        index += 2

        if is_prime(index):
            primes.add(index)
            continue

        correct_proposition = False
        for prime in primes:
            square = (index - prime) / 2.0
            if int(square) == square and int(sqrt(square)) == sqrt(square):
                correct_proposition = True

        if not correct_proposition:
            found_composite = index

    print found_composite


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
