import csv


# filename = "./csv/abiturs.csv"
filename = "./csv/exam_balls.csv"

with open(filename) as f:  
    reader = csv.reader(f, delimiter=";")

    # for row in reader:
    #     print(row)

    abiturs = list(reader)[1:]  # убираем строку заголовков
    for ab in sorted(abiturs, key=lambda x: x[1]):
        print(ab)
