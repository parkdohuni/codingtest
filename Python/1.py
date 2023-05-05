import sys
from collections import deque

def bfs(x, y):
    graph[x][y] = 0
    w = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append([nx, ny])
                w += 1
                graph[nx][ny] = 0
    
    return w

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split()) for _ in range(n))]

cnt = 0
ans = 0

for i in range(n):
    for j in range(j):
        if graph[i][j] == 1:
            cnt += 1
            ans = max(bfs(i, j), ans)
            
print(cnt)
print(ans)