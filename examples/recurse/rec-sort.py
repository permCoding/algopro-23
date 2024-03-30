def merge(a, b):
    l, r, res = 0, 0, []
    while l < len(a) and r < len(b):
        if a[l] < b[r]:
            res.append(a[l])
            l += 1
        else:
            res.append(b[r])
            r += 1
    return res+b[r:] if l==len(a) else res+a[l:]

def to_sort(a):
    if len(a) < 2: return a
    mid = len(a)//2
    return merge(to_sort(a[:mid]), to_sort(a[mid:]))
    
t = [3,1,3,3,0,5]
print(to_sort(t))
