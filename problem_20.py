def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

if __name__ == '__main__':
    s = 0
    for dg in str(factorial(100)):
        s += int(dg)
    print s
