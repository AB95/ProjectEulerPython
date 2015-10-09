def func():
    ans = 0
    i = 2
    cubes = {}
    while ans == 0:
        cube = i*i*i
        digits = "".join(sorted(str(cube)))
        if digits in cubes:
            cubes[digits] += [cube]
            if len(cubes[digits]) == 5:
                ans = min(cubes[digits])
        else:
            cubes[digits] = [cube]
        i += 1
    return ans

print func()