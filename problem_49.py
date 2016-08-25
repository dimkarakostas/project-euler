from time import time
from problem_35 import is_prime


def is_list_of_permutations(ls):
    permutations = set([''.join(set(str(num))) for num in ls])
    return len(permutations) == 1


def main():
    primes = [i for i in range(1000, 10000) if is_prime(i)]
    primes_set = set(primes)
    found_lists = []

    while len(found_lists) < 2:
        first_prime = primes[0]
        primes.pop(0)
        for p in primes:
            prime_list = [first_prime]
            diff = p - first_prime
            if p + diff in primes_set:
                prime_list += [p, p+diff]
                if is_list_of_permutations(prime_list):
                    found_lists.append(prime_list)

    print ''.join([str(i) for i in found_lists[1]])


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
