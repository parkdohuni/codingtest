import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        s = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[s] + 1
                q.append(i)

visited = [False] * (n + 1)
dist = [0] * (n + 1)
bfs(1)
big = max(dist)
print(dist.index(big), big, dist.count(big), end=" ")