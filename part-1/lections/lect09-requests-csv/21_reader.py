import csv


filename = "./csv/exam_balls.csv"
# filename = "http://files-pcoding.1gb.ru/csv?filename=exam_balls.csv"

with open(filename, 'r', encoding="utf8") as f:  
    reader = csv.reader(f, delimiter=";")

    # for row in reader:
    #     print(row)

    lst = list(reader)[1:]  # убираем строку заголовков
    for item in sorted(lst, key=lambda x: x[1]):
        if len(item) > 0:
            print(item)
