# import Euler10
# from multiprocessing import Pool
from math import log

@profile
def func():
    # primes = Euler10.func(10)
    f = file("/home/bouch/Downloads/Euler99.txt", "r")
    nums = [i.split(",") for i in f]
    # nums = nums[0:20]
    # print nums
    f.close()

    leng = len(nums)

    for i in xrange(leng):
        if i < leng - 1:
            # should be leng - 1
            nums[i][1] = nums[i][1][:-1]
        nums[i][0] = int(nums[i][0])
        nums[i][1] = int(nums[i][1])
    print "Section 1 done"

    mults = [i[1] * log(i[0]) for i in nums]
    return mults.index(max(mults))+1

    # pool = Pool(processes = 8)

    # def reduce(i):
    #     iter = 0
    #     while iter < 5:
    #         if i[1] == 1:
    #             break
    #         for j in primes:
    #             if i[1] % j == 0:
    #                 i[1] /= j
    #                 i[0] **= j
    #         iter += 1
    #     return i

    # def power(i):
    #     x = i[0]
    #     n = i[1]
    #
    #     exp = bin(n)[3:]
    #     ans = x
    #
    #     for i in xrange(exp.count("1")):
    #         ans **= 2
    #
    #     ans *= x
    #
    #     for i in xrange(exp.count("0")):
    #         ans **= 2
    #
    #     return ans


    # nums2 = map(reduce, nums)
    # print "Section 2 done"
    # mults = pool.map(power, nums)
    # mults = [power(i) for i in nums2]
    # print "Section 3 done"
    # return mults.index(max(mults))+1
print func()


