from time import time


def main():
    fractional_part = ''

    i = 1
    while len(fractional_part) < 1000000:
        fractional_part += str(i)
        i += 1

    prod = 1
    for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        prod *= int(fractional_part[i-1])
    print 'Product:', prod


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
