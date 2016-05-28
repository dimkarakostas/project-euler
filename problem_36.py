from time import time


def is_palindrome(s):
    for idx in range(len(s)/2):
        if s[idx] != s[-1*idx - 1]:
            return False
    return True


def main():
    palindrom_nums = [num for num in range(int(1e6)) if is_palindrome(str(num)) and is_palindrome(str(bin(num))[2:])]
    print 'Palindroms:', palindrom_nums
    print 'Palindrom sum:', sum(palindrom_nums)


if __name__ == '__main__':
    t = time()
    main()
    print 'Time:', time() - t
