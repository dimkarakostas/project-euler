def is_palindrome(n):
    '''
    Returns boolean value of palindrome property.
    '''
    n = str(n)
    is_pal = True
    for i in xrange(len(n)/2):
        if n[i] != n[(i+1)*(-1)]:
            is_pal = False
            break
    return is_pal

if __name__ == "__main__":
    i = j = 999
    biggest_palindrome = 0
    break_point = 0
    for i in xrange(999, 1, -1):
        if i <= break_point:
            break
        for j in xrange(999, 1, -1):
            if is_palindrome(i*j):
                break_point = j
                if i*j > biggest_palindrome:
                    biggest_palindrome = i*j
                break
    print biggest_palindrome
