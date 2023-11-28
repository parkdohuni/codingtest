import sys
from collections import deque

input = sys.stdin.readline

answer = 0
def bfs():
    q = deque()
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    for a in range(h):
        for b in range(n):
            for c in range(m):
                if arr[a][b][c] == 1 and visited[a][b][c] == 0:
                    q.append((a, b, c))
                    visited[a][b][c] = True
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if arr[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                q.append((nx, ny, nz))
                arr[nx][ny][nz] = arr[x][y][z] + 1
                visited[nx][ny][nz] = True


m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

bfs()

for a in arr:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer - 1)
