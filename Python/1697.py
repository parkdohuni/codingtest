import sys
from collections import deque

def bfs(n ,m):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == m:
            print(visited[x])
            break
        for nx in (x - 1, x + 1, x * 2):
           if 0 <= nx <= 100001 and not visited[nx]:
               visited[nx] = visited[x] + 1
               q.append(nx) 

n, m = map(int, sys.stdin.readline().split())
visited = [1] * 100001
bfs(n, m)