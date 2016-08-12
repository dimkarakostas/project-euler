from time import time
from itertools import permutations

DIGITS = '1234567890'
DIVS = [2, 3, 5, 7, 11, 13, 17]


def check_divs(pandigital):
    for i in range(1, 8):
        if int(pandigital[i:i+3]) % DIVS[i-1]:
            return False
    return True


def main():
    print sum(
        [int(''.join(p)) for p in permutations(DIGITS) if check_divs(''.join(p))]
    )

if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
