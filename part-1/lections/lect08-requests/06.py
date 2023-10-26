import module as m


filename = "https://pcoding.ru/csv/01.txt"
primes = m.get_primes(m.get_lines(filename, 0))
print(sorted(primes))
