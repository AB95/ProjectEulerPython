def euler6(n):
    return abs(square_of_sums(n) - sum_of_squares(n))


def sum_of_squares(n):
    return sum([i**2 for i in xrange(n+1)])


def square_of_sums(n):
    return sum([i for i in xrange(n+1)]) ** 2


print euler6(100)
