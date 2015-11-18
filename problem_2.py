fib = [1]
i = 1
sum = 0
while i < 4000000:
    fib.append(i)
    i += fib[-2]
    sum += i if (i % 2 == 0) else 0
print sum
