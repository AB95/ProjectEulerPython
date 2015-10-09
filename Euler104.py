


def func():
    nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    x = 1
    y = 1
    while (not is_pan(str(y)[:9], nums) or not is_pan(str(y)[-9:], nums)):
        x = y
        y += x

    return y


def is_pan(x, nums):
    if len(x) == 9 and len(set(x)) == 9:
        for i in x:
            if i not in nums:
                return False
        return True
    return False

print func()