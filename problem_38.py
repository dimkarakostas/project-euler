from time import time
from itertools import permutations


DIGITS = 123456789


def is_pandigital_product(num):
    for l in range(1, len(str(num))):
        candidate_num = int(str(num)[0:l])

        if candidate_num > 2 * int(str(num)[l:]):
            break

        product_idx = 2
        products = [str(candidate_num)]

        try:
            while True:
                product = product_idx * candidate_num
                start_product = len(''.join(products))

                if product != int(str(num)[start_product:start_product + len(str(product))]):
                    break

                products.append(str(product))
                product_idx += 1

        except ValueError:
            print 'Products:', products
            return True

    return False


def main():
    pandigitals = sorted([int('9' + ''.join(p)) for p in permutations(str(DIGITS)[:-1])], reverse=True)
    for candidate in pandigitals:
        if is_pandigital_product(candidate):
            break
        else:
            candidate -= 1
    print 'Max pandigital concatenated product:', candidate


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
