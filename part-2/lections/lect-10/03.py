from timeit import default_timer as dt
from random import randint as rnd

def sort_bubble(nums):
    for j in range(0, len(nums)-1):
        for i in range(0, len(nums)-1 -j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


def sort_select(nums):
    pass

def sort_merge(nums):
    pass

x = list(range(1_000, 8_000, 1_000))

y = []
for count in range(1_000, 8_000, 1_000):
    nums = [rnd(1, 10_000) for _ in range(count)]

    start = dt()
    sort_bubble(nums)
    finish = dt()
    
    y.append( round(finish-start, 3) )

for i in range(len(x)): print(x[i], y[i])

"""
1000 0.112
2000 0.461
3000 1.075
4000 2.145
5000 3.824
6000 4.344
7000 5.994
"""