import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dic = {}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque([start])
    while q:
        s = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                visited[i] = [True]
                dist[i] = dist[s] + 1
                q.append(i)


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    bfs(i)
    res = sum(dist) - dist[i]
    dic[i] = res

new_dict = sorted(dic, key=lambda x: dic[x])[:1]
print(*new_dict)
