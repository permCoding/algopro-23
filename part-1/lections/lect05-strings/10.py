def get_pal(s):
    if s == s[::-1]:
        return True
    else:
        return False


def get_pal_(s):  # тернарная условная операция
    return True if s == s[::-1] else False


def get_pal__(s):  # тернарная условная операция
    return s == s[::-1]


# palindrom
s = "Топот"
print(get_pal(s))
print(get_pal_(s))
print(get_pal__(s))
