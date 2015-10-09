from time import time

# def check(x):
#     if x % 10 != 0:
#         y = int(str(x)[::-1])
#         num = x + y
#         while num > 0:
#             # print num
#             if num % 2 == 0:
#                 return False
#             num /= 10
#         return True
#
#
# def func(x):
#     count = 0
#     for i in xrange(x):
#         if check(i):
#             count += 1
#     return count
#
# start = time()
# print func(1000)
# print time() - start

# x where limit is 10**x
def func(x):
    count = 0
    for i in xrange(2, x+1):
        if i % 2 == 0:
            count += 20 * (30 ** (i/2-1))
        elif i % 4 == 3:
            count += 100 * (500 ** (i/4))
    return count

print func(9)
