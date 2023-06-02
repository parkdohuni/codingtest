import sys

n = int(sys.stdin.readline())
visited1 = [0] * n
visited2 = [0] * (n + (n - 1))
visited3 = [0] * (n + (n - 1))
ans = 0


def queen(a):
    global ans
    if a == n:
        ans += 1
        return
    for i in range(n):
        if visited1[i] or visited2[i + a] or visited3[a - i + n - 1]:
            continue
        visited1[i] = 1
        visited2[i + a] = 1
        visited3[a - i + n - 1] = 1
        queen(a + 1)
        visited1[i] = 0
        visited2[i + a] = 0
        visited3[a - i + n - 1] = 0


queen(0)
print(ans)