from time import time

DIGITS = 9


def calculate_pandigitals():
    pandigitals = set()
    for multiplicand in range(2, 99):
        for multiplier in range(123, 9876/multiplicand):
            product = multiplicand*multiplier
            identity = str(multiplicand) + str(multiplier) + str(product)
            if '0' not in identity and len(identity) == len(set(identity)) == DIGITS:
                pandigitals.add(product)
    return pandigitals

t = time()
pandigitals = calculate_pandigitals()
print 'Sum:', sum(pandigitals)
print 'Time:', time() - t
