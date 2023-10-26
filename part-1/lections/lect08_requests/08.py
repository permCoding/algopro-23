import module as m


filename = "https://pcoding.ru/csv/12-sep.txt"
lines = m.get_lines(filename)
print(m.get_primes(lines[0], ";"))

# count = 0
# for line in lines:
#     count += len(m.get_primes(line, ";"))
# print(count)

"""
доработать в модуле функцию
брать только не пустые строки из исходного файла
"""