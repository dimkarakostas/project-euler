for i in range(1, 500):
    for j in range(1, 500):
        k = 1000 - i - j
        if k*k == i*i + j*j:
            print i*j*k
            exit(0)
