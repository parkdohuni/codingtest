import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((1, nvisited, 1))
    while q:
        subway, visited, level = q.popleft()
        if subway == n:
            print(level)
            sys.exit()
        for i in graph[subway]:
            if not visited[i]:
                visited[i] = True
                if i > n:
                    q.append((i, visited, level))
                else:
                    q.append((i, visited, level + 1))


n, k, m = map(int, input().split())

graph = [[] for _ in range(n + m + 1)]
for i in range(1, m + 1):
    sub = list(map(int, input().split()))
    graph[n + i].append(sub)
    for s in sub:
        graph[s].append(n + i)

nvisited = [False] * (n + m + 1)
bfs()
print(-1)
