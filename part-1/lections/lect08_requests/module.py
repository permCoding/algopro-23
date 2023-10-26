import requests


def get_lines(filename, ind=-1):
    """
    если ind не указан, то возвращай все строки  
    если ind указан, то возвращай строку по индексу  
    """
    response = requests.get(filename)
    response.encoding = "utf8"
    if ind < 0:
        return response.text.split('\n')
    else:
        return response.text.split('\n')[ind]


def get_primes(line, sep=" "):
    return [int(elm) for elm in line.split(sep) if is_prime(int(elm))]


def is_prime(num):
    if num < 2: return False
    for d in range(2, num):
        if num % d == 0:
            return False
    return True

