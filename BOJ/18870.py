import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
sort_a = sorted(a)
b = []
b.append(sort_a[0])
idx = 1
for i in range(1, len(a)):
    if sort_a[i] != b[idx - 1]:
        b.append(sort_a[i])
        idx += 1
ans = []
for A in a:
    st = 0
    en = len(b) - 1
    mid = (st + en) // 2
    while st <= en:
        mid = (st + en) // 2
        if A == b[mid]:
            ans.append(mid)
            break
        elif A < b[mid]:
            en = mid - 1
        elif A > b[mid]:
            st = mid + 1

print(*ans, end=" ")

# 5
# 2 4 -10 4 -9

# 6
# 1000 999 1000 999 1000 999