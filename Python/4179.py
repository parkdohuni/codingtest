import sys
from collections import deque

def bfs():
    
    q = deque()
    f = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                q.append([i, j])
                j_visited[i][j] = 1
            elif graph[i][j] == 'F':
                f.append([i, j])
                f_visited[i][j] = 1
                
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while f:
        fx, fy = f.popleft()
        for l in range(4):
            fnx = fx + dx[l]
            fny = fy + dy[l]
            if 0 <= fnx < r  and 0 <= fny < c: 
                if not graph[fnx][fny] == '#' and not f_visited[fnx][fny]:
                    f_visited[fnx][fny] = f_visited[fx][fy] + 1
                    f.append([fnx, fny])
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if not j_visited[nx][ny] and graph[nx][ny] != '#':
                    if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        q.append([nx, ny])
            else:
                return j_visited[x][y]
    
    return 'IMPOSSIBLE'
        
r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
f_visited, j_visited = [[0] * c for _ in range(r)], [[0] * c for _ in range(r)]

print(bfs())