from random import randint
from datetime import datetime
from timeit import default_timer


def get_sek(t):
    h, m, s = t.split(':')
    sek = int(h)*60*60 + int(m)*60 + float(s)
    return sek


def get_sorted(lst):
    for j in range(0, len(lst)-1):
        for i in range(0, len(lst)-j-1):
            if lst[i] > lst[i+1]: lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


cnt = 10_000
seq = [randint(1, 10_000) for _ in range(cnt)]

start_time = default_timer() 
start_dt = str(datetime.now()).split()[1]

lst = get_sorted(seq)

stop_time = default_timer()
stop_dt = str(datetime.now()).split()[1]

print(f"{round(stop_time - start_time, 2)}")
print(f"{round(get_sek(stop_dt) - get_sek(start_dt), 2)}")

# print(lst)
