from time import time
import fractions


def digit_cancel():
    digit_cancelling_fractions = []
    for numerator in range(10, 100):
        for denominator in range(numerator+1, 100):
            if not (numerator % 10 or denominator % 10):
                continue
            frac = fractions.Fraction(numerator, denominator)
            for digit in str(numerator):
                if digit in str(denominator):
                    num = int(str(numerator).replace(digit, '', 1))
                    denom = int(str(denominator).replace(digit, '', 1))
                    try:
                        if frac == fractions.Fraction(num, denom):
                                digit_cancelling_fractions.append((numerator, denominator, frac))
                    except ZeroDivisionError:
                        break
    return digit_cancelling_fractions


t = time()

digit_cancelling_fractions = digit_cancel()

print 'Fractions:'
product = fractions.Fraction(1, 1)
for fr in digit_cancelling_fractions:
    product *= fr[2]
    print '\t{}/{} = {}'.format(fr[0], fr[1], fr[2])
print 'Product:', product

print 'Time:', time() - t
