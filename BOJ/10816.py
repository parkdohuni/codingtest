import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a = sorted(a)
ans = {}
for A in a:
    if A not in ans:
        st = 0
        en = n - 1
        while st <= en:
            mid = (st + en) // 2
            if a[mid] == A:
                ans[A] = a[st:en + 1].count(A)
                break
            elif a[mid] > A:
                en = mid - 1
            elif a[mid] < A:
                st = mid + 1

print(' '.join(str(ans[x]) if x in ans else '0' for x in b))

# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10