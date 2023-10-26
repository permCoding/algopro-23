def get_line_ind(filename, ind=0):
    return open(filename, "r", encoding="utf8").readlines()[ind]


def get_primes(line):
    return [int(elm) for elm in line.split() if is_prime(int(elm))]


def is_prime(num):
    if num < 2: return False
    for d in range(2, num):
        if num % d == 0:
            return False
    return True


filename = "./txt/01.txt"
primes = get_primes(get_line_ind(filename))
print(sorted(primes))
print(len(primes))
print(sum(primes))
