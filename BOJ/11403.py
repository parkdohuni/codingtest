import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start, visited, ans):
    q = deque([start])

    while q:
        s = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                ans[start][i] = 1
                q.append(i)



n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
graph = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            graph[i].append(j)

ans = [[0] * n for _ in range(n)]
for k in range(n):
    visited = [False] * (n + 1)
    bfs(graph, k, visited, ans)

for row in ans:
    print(" ".join(map(str, row)))