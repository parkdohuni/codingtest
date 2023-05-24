import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
visited = [0] * n
ans = 0
add = 0


def dfs(idx, add):
    global ans
    if idx >= n:
        return
    add += arr[idx]
    if add == s:
        ans += 1
    # visited[idx] = 1
    dfs(idx + 1, add)


dfs(0)
print(ans)
