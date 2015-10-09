import pyximport; pyximport.install()
import cpriimes
import itertools as it

itp = it.permutations

allprimes = cpriimes.func(10000)
primes = filter(lambda x: x > 999, cpriimes.func(10000))
primeset = set(primes)

def isPrime(x):
    if cpriimes.isPrime(x, allprimes):
        return True
    return False

def permuts(x):
    nums = list(set([i for i in itp(str(x))]))
    for j in xrange(len(nums)):
        nums[j] = int("".join(nums[j]))
    return sorted(nums)

def seq(x):
    nums = [i for i in permuts(x) if isPrime(i)]
    maxcount = 0
    num = 0
    finalli = 0
    for i in nums:    
        for j in xrange(2, 4500, 2):
            count = 0
            i2 = i
            if i + j in nums:
                count += 1
                i2 += j
                while i2 + j in nums:
                    count += 1
                    i2 += j
                if count > maxcount:
                    maxcount = count
                    num = j
                    finalli = i
    if maxcount > 1:
        return (finalli, num, maxcount)
#            if i + j in nums and i + j + j in nums:
#                return j

final = [j for j in list(set([seq(i) for i in primes if seq(i) and len(str(seq(i)[0]))==4 and seq(i) != 1487]))]
print str(final[0][0]) + str(final[0][0] + final[0][1]) + str(final[0][0] + final[0][1] + final[0][1])
#for i in primes:
#    if seq(i):
#        print seq(i)