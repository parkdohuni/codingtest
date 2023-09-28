import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n + 1)
arr = []


def back(idx):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    else:
        for i in range(idx, n + 1):
            # if visited[i]:
            #     continue
            # visited[i] = True
            arr.append(i)
            back(i)
            arr.pop()
            # visited[i] = False


back(1)
