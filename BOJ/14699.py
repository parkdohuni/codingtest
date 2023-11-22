import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[0] * (m + 1) for _ in range(m + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

for i in graph:
    print(i)
