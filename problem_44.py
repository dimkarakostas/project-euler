from time import time


def pentagonal(n):
    return (n*(3*n - 1)) / 2


def main():
    checked_pentagonals = set([1])
    found_couple = False

    pentagonal_gen = (x for x in range(2, 1000000) if not found_couple)

    for index in pentagonal_gen:
        check_sum = pentagonal(index)

        for upper_couple_part in checked_pentagonals:
            lower_couple_part = check_sum - upper_couple_part
            if lower_couple_part in checked_pentagonals:
                check_diff = upper_couple_part - lower_couple_part
                if check_diff in checked_pentagonals:
                    couple = (lower_couple_part, upper_couple_part)
                    found_couple = True
                    break

        checked_pentagonals.add(check_sum)

    print couple, couple[1] - couple[0]


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
