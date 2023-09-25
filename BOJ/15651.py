import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n + 1)
arr = []


def back():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    else:
        for i in range(1, n + 1):
            visited[i] = True
            arr.append(i)
            back()
            arr.pop()
            visited[i] = False


back()
