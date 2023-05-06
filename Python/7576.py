import sys
from collections import deque

def bfs(x, y):
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append([i, j])
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                q.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1
                
m, n = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


bfs(0, 0)
flag = 0
for i in range(n):
    if flag == 1:
        break
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            flag = 1
            break

if not flag == 1:
    ans = max(map(max, arr))
    print(ans - 1)
            
