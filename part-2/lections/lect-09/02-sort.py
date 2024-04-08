from module_sorting import get_sorted_list as gsl
# from timeit import timeit  # ver_1
from datetime import datetime  # ver_2
from random import randint as rnd


# nums = [8,2,1,5,4,6,0,0,0,99]
# nums = [5,2,1,14,26,30,1,1,40,50,99]
nums = [rnd(1, 10_000) for _ in range(20_000)]

print(nums[:20])

start_time = str(datetime.now()).split()[1]
res = gsl(nums)
stop_time = str(datetime.now()).split()[1]
print(stop_time, '\n', start_time)

print(res[:20])
