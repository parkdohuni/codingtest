import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True
    friends = [1] + graph[1]
    ans = []
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i] and a in friends:
                queue.append(i)
                visited[i] = True
                ans.append(i)
    print(len(ans))

bfs(graph, 1, visited)