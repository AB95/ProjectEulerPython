def is_prime(n):
    if n <= 1:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    d = 2

    while i*i <= n:
        if n % i == 0:
            return False

        i += d
        d = 6 - d

    return True