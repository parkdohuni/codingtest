import sys

read = sys.stdin.readline

n, m = map(int, read().split())
A = set(map(int, read().split()))
B = set(map(int, read().split()))

ans = A - B
ans = sorted(ans)
print(len(ans))
if len(ans) != 0:
    print(*ans)
