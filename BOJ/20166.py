import sys
from collections import deque

read = sys.stdin.readline
n, m, k = list(map(int, read().split()))
arr = []
for _ in range(n):
    arr.append(list(read().rstrip()))
dic = dict()


def bfs(x: int, y: int):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    queue = deque()
    queue.append((x, y, arr[x][y]))
    while queue:
        x, y, string = queue.popleft()

        if string not in dic:
            dic[string] = 1
        else:
            dic[string] += 1

        if len(string) >= 5:
            continue

        for i in range(8):
            ax = x + dx[i]
            ay = y + dy[i]
            if ax < 0:
                ax = n - 1
            elif ax == n:
                ax = 0
            if ay < 0:
                ay = m - 1
            elif ay == m:
                ay = 0
            queue.append((ax, ay, string + arr[ax][ay]))


ans = []

for i in range(n):
    for j in range(m):
        bfs(i, j)

for _ in range(k):
    god = read().rstrip()
    if god in dic:
        ans.append(dic[god])
    else:
        ans.append(0)

for an in ans:
    print(an)
