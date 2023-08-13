import sys
from collections import deque

n, m, start = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

def dfs(graph, start, visited, ans):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            ans.append(i)
            dfs(graph, i, visited, ans)


def bfs(graph, start, visited):
    ans = [start]
    visited[start] = True
    queue = deque([start])

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                ans.append(i)
                visited[i] = True
                queue.append(i)
    print(" ".join(map(str, ans)))


visited = [False] * (n + 1)
ans = [start]
dfs(graph, start, visited, ans)
print(" ".join(map(str, ans)))

visited = [False] * (n + 1)
bfs(graph, start, visited)
