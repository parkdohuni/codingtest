import sys

read = sys.stdin.readline

n = int(read())
a = []
for _ in range(n):
    a.append(int(read()))

two = []
for i in range(n):
    for j in range(i, n):
        two.append(a[i] + a[j])
sort_two = sorted(two)
ans = 0
for l in range(n):
    for k in range(n):
        target = a[l] - a[k]
        if target > 0:
            st = 0
            en = len(two) - 1
            while st <= en:
                mid = (st + en) // 2
                if sort_two[mid] == target:
                    if ans < a[l]:
                        ans = a[l]
                    break
                elif sort_two[mid] < target:
                    st = mid + 1
                elif sort_two[mid] > target:
                    en = mid - 1

print(ans)