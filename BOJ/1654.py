import sys

read = sys.stdin.readline

k, n = map(int, read().split())
a = [int(read()) for _ in range(k)]
st = 1
en = max(a)

while st <= en:
    mid = (st + en) // 2
    line = 0
    for i in a:
        line += i // mid
    if line >= n:
        st = mid + 1
    else:
        en = mid - 1
print(en)
