from math import sqrt

DIV = 500


def calc(n):
    dvs = 0
    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            dvs += 2
    return dvs

outp = 0
t = 0
while True:
    t += outp
    if calc(t) > DIV:
        break
    outp += 1
print t
