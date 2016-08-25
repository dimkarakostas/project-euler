from time import time


def main():
    max = 1000
    print str(sum([i**i for i in range(1, max+1)]))[-10:]


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
