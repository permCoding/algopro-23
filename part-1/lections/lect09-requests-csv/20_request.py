import requests
import csv


filename = "https://pcoding.ru/csv/abiturs.csv"
filename = "http://files-pcoding.1gb.ru/csv?filename=abiturs.csv"

response = requests.get(filename)
response.encoding = "utf8"
lines = response.text.split("\n")

# for line in lines: print(line)
    
reader = csv.reader(lines, delimiter=",")

headers = next(reader)  # читаем строку заголовков
print(f'headers => {",".join(headers)}')

for row in reader: print(row)
