import sys
from collections import deque

def bfs(x, y):
    arr[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    w = 1 # 넓이
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] = 0
                w += 1
    return w

n, m = map(int, sys.stdin.readline().split())

arr = [list(map(int, input().split())) for _ in range(n)]
 
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            ans = max(bfs(i, j), ans)

print(cnt)
print(ans)