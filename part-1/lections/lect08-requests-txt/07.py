import module as m


filename = "https://pcoding.ru/csv/12.txt"
lines = m.get_lines(filename)

count = 0
for line in lines:
    count += len(m.get_primes(line))
print(count)
