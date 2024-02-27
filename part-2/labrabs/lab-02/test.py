words = ['12312', '1e2dwedwd111', '343']

mx0 = 0
for word in words:
    if len(word) > mx0:
        mx0 = len(word)
    
mx1 = 0
for word in words:
    mx1 = max(mx1, len(word))

mx2 = len(max(words, key=lambda x: len(x)))

def func(word):
    # return word.count('o')
    return len(word)
mx3 = len(max(words, key=func))

mx4 = len(max(words, key=len))

print(mx0, mx1, mx2, mx3, mx4)