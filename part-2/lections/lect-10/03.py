from timeit import default_timer as dt
from random import randint as rnd

def sort_bubble(nums):
    for j in range(0, len(nums)-1):
        for i in range(0, len(nums)-1 -j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


nums = [rnd(1, 10_000) for _ in range(10_000)]  # asc 20_000 -> 40 sec

start = dt()
srtd = sort_bubble(nums)
finish = dt()
print(round(finish-start, 3))
# print(srtd)
