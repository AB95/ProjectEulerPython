from is_prime import is_prime


def euler7(n):
    if n == 1:
        return 2

    num = 1
    i = 1

    while i < n:
        num += 2
        if is_prime(num):
            i += 1

    return num
