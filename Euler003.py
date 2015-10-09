def euler3(n):
    largest = 0
    while n % 2 == 0:
        largest = 2
        n /= 2

    i = 3
    while n > 1:
        if n % i == 0:
            if i > largest:
                largest = i
            n /= i
        else:
            i += 2

    if n > largest:
        largest = n

    return largest
