import csv


filename = "./csv/abiturs.csv"
# filename = "./csv/exam_balls.csv"

with open(filename, "r", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    rows = list(reader)
    titles = rows[0]  # заголовки
    abiturs = rows[1:]  # данные
    
    ab_sorted = sorted(abiturs, key=lambda x: x[2], reverse=True)
    # for ab in ab_sorted:
    #     print(ab)

    # titles = "id,lastName,rating,gender,birthDate,city".split(",")
    with open("./csv/result.csv", "w", encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(titles)  # записать строку заголовков
        writer.writerows(ab_sorted)  # записать все строки с данными
