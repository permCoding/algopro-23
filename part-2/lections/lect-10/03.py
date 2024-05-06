from timeit import default_timer as dt
from random import randint as rnd

def sort_bubble(nums):
    for j in range(0, len(nums)-1):
        for i in range(0, len(nums)-1 -j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


nums = [rnd(1, 10_000) for _ in range(20_000)]  # asc

start = dt()
srtd = sort_bubble(nums)
finish = dt()
print(round(finish-start, 2))
# print(srtd)
