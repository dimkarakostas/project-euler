from math import sqrt
from time import time

PRIME_STATUS = {}


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def check_prime_circles(num):
    circles = []
    s = str(num)
    for i in range(len(s)):
        circle = int(s[i:] + s[0:i])
        circles.append(circle)
        if circle not in PRIME_STATUS:
            PRIME_STATUS[circle] = is_prime(circle)
        if not PRIME_STATUS[circle]:
            return False
    return True


def main():
    circular_primes = []
    for num in range(2, 1000000):
        if check_prime_circles(num):
            circular_primes.append(num)
    print 'Circular primes:', circular_primes
    print 'Amount of circular primes:', len(circular_primes)

if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
