def tobin(n):
    if n < 1: return ''
    return tobin(n//2) + str(n%2)
def todec(b, p=0):
    if b == '': return 0
    return int(b[-1])*2**p + todec(b[:-1], p+1)
print(tobin(24))
print(todec('10011'))
