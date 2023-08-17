import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
while 1:
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, start, visited, dist):
    q = deque([start])
    visited[start] = True
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[a] + 1
                q.append(i)

ans = []
temp = 51
for i in range(1, n + 1):
    dist = [0] * (n + 1)
    visited = [False] * (n + 1)
    bfs(graph, i, visited, dist)
    big = max(dist)
    if big == temp:
        ans.append(i)
    elif big < temp:
        ans = [i]
        temp = big

print(temp, len(ans))
print(*ans)
