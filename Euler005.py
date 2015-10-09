def euler5(n):
    if n == 1:
        return 1
    elif n > 1:
        num = n * (n - 1)
        while not is_divisible(n, num):
            num += n * (n - 1)

        return num


def is_divisible(n, num):
    for i in xrange(1, n+1):
        if num % i != 0:
            return False
    return True
