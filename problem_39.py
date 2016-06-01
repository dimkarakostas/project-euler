from time import time
from math import pow, sqrt


LIMIT = 1000
PERIMETERS = [[0 for i in range(j)] for j in range(LIMIT/2)]


def most_common(lst):
    return max(set(lst), key=lst.count)


def main():
    for a in range(1, LIMIT/2):
        for b in range(a+1, LIMIT/2):
            c = sqrt(pow(a, 2) + pow(b, 2))  # Pythagorean theorem
            perimeter = a + b + c
            if c.is_integer() and perimeter < LIMIT:
                PERIMETERS[b][a] = perimeter
    print 'Maximum perimeter options:', most_common([item for sublist in PERIMETERS for item in sublist if item])


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
