def get_sum(n):
    if n == 0: return 0  # точка останова
    return n + get_sum(n-1)  # шаг рекурсии


n = 100
print(get_sum(n))  # 5050