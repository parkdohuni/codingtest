import sys
from collections import deque

def bfs():
    ans = 1
    flag = 0
    
    q = deque()
    f = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                q.append([i, j])
            elif graph[i][j] == 'F':
                f.append([i, j])
            elif graph[i][j] == '.':
                graph[i][j] = 0
                
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while 1:
        qsize = len(q)
        if qsize == 0 or graph[q[0][0]] == 'F':
            break
        for _ in range(qsize):
            x, y = q.popleft()
            cnt = 0
            
            if not graph[x][y] == 'F':
                for k in range(4):
                    cnt += 1
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        ans += graph[x][y]
                        while q:
                            q.pop()
                        break
                    if graph[nx][ny] == 0:
                        if not graph[x][y] == 'J' and not graph[x][y] == 'F' and graph[x][y] > 0:
                            graph[nx][ny] += graph[x][y] + 1
                        else:
                            graph[nx][ny] += 1
                        cnt = 0
                        flag = 0
                        q.append([nx, ny])
                    if cnt == 4:
                        flag = 1
            else:
                flag = 1
            
        fsize = len(f)
        for _ in range(fsize):
            fx, fy = f.popleft()
            for l in range(4):
                fnx = fx + dx[l]
                fny = fy + dy[l]
                if 0 <= fnx < r  and 0 <= fny < c and not graph[fnx][fny] == '#':
                    graph[fnx][fny] = 'F'
                    f.append([fnx, fny])
                            
    
    if flag == 1:
        print("IMPOSSIBLE")
    else:
        print(ans)
        
r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

bfs()