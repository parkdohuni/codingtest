import sys
from collections import deque


def bfs(x, y):
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0] for _ in range(M)]
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 0
    return 1

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1
    ans = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                ans += bfs(i, j)
    print(ans)
