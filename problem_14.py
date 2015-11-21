from time import time

THRESHOLD = 1000000
TOTAL = [0]*THRESHOLD


def calculate_collatz(n):
    chain = []
    chain_len = 0
    while n > 1:
        if n < THRESHOLD and TOTAL[n]:
            chain_len += TOTAL[n]
            break
        chain += [n]
        chain_len += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    return chain, chain_len


def main():
    start_time = time()
    tst = THRESHOLD - 1
    while tst > THRESHOLD/2:
        if TOTAL[tst] == 0:
            chain, chain_len = calculate_collatz(tst)
            while chain:
                tested = chain[0]
                chain = chain[1:]
                if tested < THRESHOLD:
                    TOTAL[tested] += chain_len
                chain_len -= 1
        tst -= 1

    m = max(TOTAL)
    for i, j in enumerate(TOTAL):
        if j == m:
            print "Finished in", time() - start_time
            print "Index", i, "Length", j
            break


if __name__ == '__main__':
    main()
