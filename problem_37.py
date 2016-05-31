from problem_35 import is_prime
from time import time


TRUNCATABLE_PRIMES = []


def is_truncatable_prime(num):
    for i in ['0', '4', '6', '8']:
        if i in str(num):
            return False

    for i in ['2', '5']:
        if i in str(num)[1:]:
            return False

    if not is_prime(num):
        return False

    for idx in range(len(str(num)) - 1):
        if not is_prime(int(str(num)[idx+1:])):
            return False

    for idx in range(len(str(num)) - 1):
        if not is_prime(int(str(num)[0:-1*idx-1])):
            return False

    return True


def main():
    counter = 11
    while len(TRUNCATABLE_PRIMES) < 11:
        counter += 2
        if is_truncatable_prime(counter):
            TRUNCATABLE_PRIMES.append(counter)
            print TRUNCATABLE_PRIMES
    print 'Sum:', sum(TRUNCATABLE_PRIMES)

if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
