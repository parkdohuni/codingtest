import sys

read = sys.stdin.readline
n, m = map(int, read().split())
a = list(map(int, read().split()))

a = sorted(a)
st = 1
en = a[-1]
while st <= en:
    total = 0
    mid = (st + en) // 2

    for i in a:
        if i - mid > 0:
            total += (i - mid)
        if total > m:
            break
    if total >= m:
        st = mid + 1
    else:
        en = mid - 1

print(en)
