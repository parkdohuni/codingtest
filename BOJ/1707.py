import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, group):
    q = deque([start])
    visited[start] = group
    while q:
        s = q.popleft()

        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = -1 * visited[s]
            elif visited[i] == visited[s]:
                return False

    return True


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (v + 1)

    for i in range(1, v + 1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')
