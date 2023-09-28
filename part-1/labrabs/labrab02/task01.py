def task_01(x, y):
    for i in range(min(x, y), max(x, y)+1):
        if i % 2 != 0:
            print(i)


a = int(input("Введите первое число - "))
b = int(input("Введите второе число - "))
task_01(a, b)