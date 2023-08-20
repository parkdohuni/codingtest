import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

re = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    re[v].append(u)


def bfs(start):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 1
    while q:
        s = q.popleft()
        for i in re[s]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt


ans = []
maxCnt = 1
for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > maxCnt:
        maxCnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == maxCnt:
        ans.append(i)

print(*ans)
