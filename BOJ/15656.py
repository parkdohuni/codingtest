import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr = sorted(arr)
visited = [False] * (n + 1)


def back(idx):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(idx, n + 1):
        # if visited[i]:
        #     continue
        # visited[i] = True
        ans.append(arr[i - 1])
        back(i)
        ans.pop()
        # visited[i] = False


back(1)
