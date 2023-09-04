import sys
from collections import deque

input = sys.stdin.readline



def bfs(start):
    global ans
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 0

    while q:
        s = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                if cnt > standard:
                    ans += 1
                    return
                q.append(i)


def re_bfs(start):
    global ans
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 0

    while q:
        s = q.popleft()
        for i in re_graph[s]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                if cnt > standard:
                    ans += 1
                    return
                q.append(i)


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
re_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    re_graph[v].append(u)
ans = 0
standard = n // 2

for i in range(1, n + 1):
    bfs(i)
    re_bfs(i)

print(ans)