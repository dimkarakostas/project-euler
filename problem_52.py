i = 1
while True:
    i += 1
    s = set(str(i))
    if len(s) < len(str(i)):
        continue
    for j in range(2, 7):
        if s.symmetric_difference(str(i * j)) or len(str(i)) != len(str(i * j)):
            s = None
            break
    if s:
        print i
        break
