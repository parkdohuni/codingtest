import sys
read = sys.stdin.readline
n, m = map(int, read().rstrip().split())
dict = {}
for _ in range(n):
    site, pw = map(str, read().rstrip().split())
    dict[site] = pw

for _ in range(m):
    s = str(read().rstrip())
    print(dict[s])