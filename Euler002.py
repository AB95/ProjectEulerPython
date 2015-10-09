def euler2(n):
    a = 0
    b = 1
    total = 0
    while b < n:
        a, b = b, a+b
        if b%2 == 0:
            total += b
    return total