import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr = sorted(arr)
visited = [False] * (n + 1)


def back():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n + 1):
        ans.append(arr[i - 1])
        back()
        ans.pop()


back()
