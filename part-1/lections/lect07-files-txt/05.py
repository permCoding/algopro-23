import requests


def get_lines_from_url(url):
    return requests.get(url).text.split('\n')


def get_column(lines, column=0, row=0, sep='\t'):
    return [line.split(sep)[column] for line in lines[row:]]


lines = get_lines_from_url('https://pcoding.ru/csv/06.txt')
langs = get_column(lines, row=3)

for lang in sorted(langs, reverse=True):
    print(lang)
