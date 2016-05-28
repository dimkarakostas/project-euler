from problem_20 import factorial
from time import time


def calculate_digit_factorials(start, end):
    known_factorials = {}
    digit_factorials = []
    for num in range(start, end):
        factorial_sum = 0
        for digit in str(num):
            if digit not in known_factorials:
                known_factorials[digit] = factorial(int(digit))
            factorial_sum += known_factorials[digit]
        if num == factorial_sum:
            digit_factorials.append(num)
    return digit_factorials

if __name__ == '__main__':
    t = time()
    digit_factorials = calculate_digit_factorials(10, 50000)
    print 'Factorials:', digit_factorials
    print 'Sum:', sum(digit_factorials)
    print 'Time:', time() - t
