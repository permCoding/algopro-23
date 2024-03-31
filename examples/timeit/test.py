from datetime import datetime
from timeit import default_timer


def gen_nums_uniq_odd(n):
    lst = []
    while len(lst) < n:
        tm = str(datetime.now()).split()[1].split('.')[0]        
        if tm not in lst:
            lst.append(tm)
    return lst

         
start_time = default_timer() 
lst = gen_nums_uniq_odd(4)
stop_time = default_timer()

all_time = stop_time - start_time

print(f"{round(all_time, 2)}")
print(len(lst))
print(lst)
