import sys

read = sys.stdin.readline
n, p, q = list(map(int, read().split()))

a = dict()
a[0] = 1
temp = 0

def dfs(n):
    if n in a:
        return a[n]
    else:
        a[n] = dfs(n // p) + dfs(n // q)
        return a[n]


print(dfs(n))
