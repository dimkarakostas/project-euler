def is_palindrome(num):
    num = str(num)
    for i in xrange(len(num) / 2):
        if num[i] != num[-1 * (i + 1)]:
            return False
    return True

lychrel_nums = 0
for num in xrange(10001):
    flag, temp = True, num
    for i in xrange(50):
        temp += int(str(temp)[::-1])
        if is_palindrome(temp):
            flag = False
            break
    lychrel_nums += 1 if flag else 0

print(lychrel_nums)
