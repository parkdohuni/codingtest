import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
ans = []
visited = [False] * (n + 1)


def back(idx):
    if len(ans) == m:
        print(*ans)
        return
    flag = 0
    for i in range(idx, n + 1):
        if not visited[i] and flag != arr[i - 1]:
            visited[i] = True
            ans.append(arr[i - 1])
            flag = arr[i - 1]
            back(i)
            ans.pop()
            visited[i] = False


back(1)
