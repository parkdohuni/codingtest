import sys
from collections import deque


def bfs(start):
    visited = [False] * (n + 1)
    cnt = 1
    q = deque([(start, cnt)])
    while q:
        cur, cnt = q.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for i in graph[cur]:
            if not visited[i] and height[i] > height[cur]:
                cnt += 1
                q.append((i, cnt))

    return cnt


input = sys.stdin.readline

n, m = map(int, input().split())
height = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    result = bfs(i)
    print(result)
