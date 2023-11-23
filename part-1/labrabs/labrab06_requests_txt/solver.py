import requests


def get_lines_from_url(url):
    """получить список строк из файла по адресу"""
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text.split('\n')


url = "https://pcoding.ru/csv/exam03.txt"
lines = get_lines_from_url(url)

# найти студента с худшим рейтингом
lst = [line.split(',') for line in lines[1:]]
lst.sort(key=lambda x: int(x[2]))
print(lst[0])
