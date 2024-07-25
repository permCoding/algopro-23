import time
import random


def merge(left_half, right_half):
    i = j = 0  # позиции в левой, правой половинах
    
    union = []
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            union += [left_half[i]]
            i += 1
        else:
            union += [right_half[j]]
            j += 1
            
    return union + left_half[i:] + right_half[j:]


def merge_sort(arr):
    if len(arr) <= 1: return arr
    
    mid = len(arr) // 2
    
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)


if __name__ == "__main__":
    # Генерация списка уникальных случайных чисел
    lst = random.sample(range(1, 20001), 30)
    print(lst)
    t0 = time.time()  #Начало отсчета времени
    sort_list = merge_sort(lst)  #Запуск сортировки
    print(time.time()-t0, " Время выполнения")  #Вычисление времени работы
    print(sort_list)
