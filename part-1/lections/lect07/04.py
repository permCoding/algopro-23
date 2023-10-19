def get_lines(filename):
    return [line.strip() for line in open(filename)]


def get_column(lines, column=0, row=0, sep='\t'):
    return [line.split(sep)[column] for line in lines[row:]]


lines = get_lines('./data/06.txt')
langs = get_column(lines, row=3)

for lang in sorted(langs):
    print(lang)

# https://pcoding.ru/csv/06.txt