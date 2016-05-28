from time import time

TARGET_SUM = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

DYNAMIC_TABLE = {}


def calculate(point, coinset):
    if point - coinset[0] < 0:
        return 0
    elif point == coinset[0]:
        return 1
    else:
        if (point, str(coinset)) in DYNAMIC_TABLE:
            return DYNAMIC_TABLE[(point, str(coinset))]
        DYNAMIC_TABLE[(point, str(coinset))] = calculate(point-coinset[0], coinset) + calculate(point, coinset[1:])
        return DYNAMIC_TABLE[(point, str(coinset))]

t = time()
print calculate(TARGET_SUM, COINS)
print 'Time:', time()-t
