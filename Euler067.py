import time

def func():
    f = file("/home/bouch/Downloads/Euler67.txt", "r")
    nums = f.read().split("\n")
    nums = [i.split(" ") for i in nums]
    nums.pop(100)
    for i in xrange(len(nums)):
        nums[i] = [int(j) for j in nums[i]]
        
    for i in range(len(nums)-2, -1, -1):
        nums[i] = [nums[i][j]+max(nums[i+1][j:j+2]) for j in xrange(len(nums[i]))]
    f.close()
    return nums[i][0]
    
start = time.time()
print func()
print time.time() - start