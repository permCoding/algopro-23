import requests


def get_line_ind(filename, ind=0):
    response = requests.get(filename)
    response.encoding = "utf8"
    return response.text.split('\n')[ind]


def get_primes(line):
    return [int(elm) for elm in line.split() if is_prime(int(elm))]


def is_prime(num):
    if num < 2: return False
    for d in range(2, num):
        if num % d == 0:
            return False
    return True


filename = "https://pcoding.ru/csv/01.txt"
primes = get_primes(get_line_ind(filename))
print(sorted(primes))
