def euler4(n):
    x = 10**n - 1
    y = x
    largest = 0
    
    while y > 10**(n-1):
        while x > 10**(n-1):
            if is_palindromic(x*y):
                if x*y > largest:
                    largest = x*y
            x -= 1

        x = 999
        y -= 1

    return largest


def is_palindromic(f):
    if str(f) == str(f)[::-1]:
        return True
