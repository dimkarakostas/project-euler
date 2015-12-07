from time import time


def get_cycle(res_list, res):
    for i, rs in enumerate(res_list):
        if rs == res:
            return len(res_list[i:])
    return -1


def get_res(divident, divisor):
    qt = divident / divisor
    md = divident % divisor
    if qt:
        res = str(qt) + ' ' + str(md)
        divident -= qt*divisor
    else:
        divident *= 10
        if divident < divisor:
            res = '0 ' + str(md)
        else:
            res = None
    return res, divident


if __name__ == '__main__':
    max_cycle = 0
    max_num = 0
    t = time()
    for divisor in range(2, 1000):
        divident = 1
        res_list = []
        res_set = set()
        ln = -1
        while ln < 0:
            res, divident = get_res(divident, divisor)
            if res:
                if res in res_set:
                    ln = get_cycle(res_list, res)
                    if ln > max_cycle:
                        max_cycle = ln
                        max_num = divisor
                res_list.append(res)
                res_set.add(res)
    print 'Value:', max_num, 'Cycle:', max_cycle, 'Time:', time() - t
