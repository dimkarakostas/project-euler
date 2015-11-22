'''
File: problem_15.py
Author: dimkarakostas
Description: The problem is equivalent to calculating the distribution of n distinct objects (move choices) to k non-distinct places (moves right/down that are needed to reach the end). Given a mxm matrix, n=2*m and k=m, since you need exactly 2*m moves (m right and m down) to reach the end.
'''

DIMENSION = 20


def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def combinations(n):
    return factorial(2*n) / (factorial(2*n-n) * factorial(n))


def main():
    print combinations(DIMENSION)


if __name__ == '__main__':
    main()
