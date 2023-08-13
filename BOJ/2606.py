import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    ans = 0
    while queue:
        s = queue.popleft()
        for i in graph[s]:
            if not visited[i]:
                ans += 1
                visited[i] = True
                queue.append(i)
    print(ans)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

bfs(graph, 1, visited)