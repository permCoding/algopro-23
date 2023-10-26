def to_number_lst(dec, base=2):
    lst = []
    while dec > 0:
        lst.append(dec % base)
        dec //= base
    result = ""
    for elm in lst[::-1]:
        result += str(elm)
    return result

def to_number_lst_(dec, base=2):
    lst = []
    while dec > 0:
        lst.append(dec % base)
        dec //= base
    return "".join(map(str, lst[::-1]))

def to_number_str(dec, base=2):
    """ 
    функция перевода в систему счисления с основанием base
    """
    result = ""
    while dec > 0:
        result = str(dec % base) + result
        dec //= base
    return result

def to_number_divmod(dec, base=2):
    result = ''
    while dec > 0:
        dec, mod = divmod(dec, base)
        result = str(mod) + result
    return result

def to_number_rec(dec, base=2):
    if dec == 0: return ""
    return to_number_rec(dec//base, base) + str(dec%base)

# 12 => 1100
# 12 // base = 6 | 12 % 2 = 0
# 6 // base = 3 | 6 % base = 0
# 3 // base = 1 | 3 % base = 1
# 1 // base = 0 | 1 % base = 1
# divmod ========

dec = 19
print(to_number_str(dec))
print(to_number_divmod(dec))
print(to_number_rec(dec))