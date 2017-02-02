from time import time
from prime_functions import get_primes_below, is_prime

MIL = 1000000

LIMIT = MIL


def main():
    primes = get_primes_below(LIMIT)

    max_sum = 0
    max_chain = []

    slow_idx = 0
    fast_idx = slow_idx
    while slow_idx < len(primes) - 1:
        fast_idx += 1

        current_chain = primes[slow_idx:fast_idx]
        current_sum = sum(current_chain)

        if current_sum > LIMIT or fast_idx == len(primes):
            slow_idx += 1
            fast_idx = slow_idx
            if len(primes[slow_idx:]) <= len(max_chain):
                break

        if is_prime(current_sum):
            if len(current_chain) > len(max_chain):
                max_chain = current_chain
                max_sum = current_sum

    print max_sum


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
