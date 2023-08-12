import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
visited = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        ans += 1

print(ans)