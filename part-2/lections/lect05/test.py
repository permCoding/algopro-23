import sys


def sm(n):
    return sm(n-1) + n


print(sys.getrecursionlimit())
sys.setrecursionlimit(12_000)
print(sys.getrecursionlimit())

print(sm(55))
