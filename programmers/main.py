from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                visited[nx][ny] = 1
                q.appendleft([nx, ny])
                cnt += 1

    return cnt


q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            q.append([i, j])
            print(bfs())
