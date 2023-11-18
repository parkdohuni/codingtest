import sys
import copy

from collections import deque


def bfs(x, y, alpha, graph):
    q = deque()
    q.append([x, y])
    nx = [1, -1, 0, 0]
    ny = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = nx[i] + x
            dy = ny[i] + y
            if 0 <= dx < N and 0 <= dy < N and graph[dx][dy] == alpha:
                q.append([dx, dy])
                graph[dx][dy] = 0


input = sys.stdin.readline
N = int(input())
arr = [list(map(str, input().rstrip())) for _ in range(N)]
arr_color = copy.deepcopy(arr)
ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr_color[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            bfs(i, j, 'R', arr)
            ans += 1
        elif arr[i][j] == 'G':
            bfs(i, j, 'G', arr)
            ans += 1
        elif arr[i][j] == 'B':
            bfs(i, j, 'B', arr)
            ans += 1
print(ans)
ans = 0
for i in range(N):
    for j in range(N):
        if arr_color[i][j] == 'R':
            bfs(i, j, 'R', arr_color)
            ans += 1
        elif arr_color[i][j] == 'B':
            bfs(i, j, 'B', arr_color)
            ans += 1
print(ans)
