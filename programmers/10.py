from collections import deque


def solution(maps):
    answer = 1
    m = len(maps[0])
    n = len(maps)
    x = y = 0
    s = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    s.append([x, y])
    maps[x][y] = 2
    flag = 0
    while s:
        x, y = s.popleft()
        if x == n - 1 and y == m - 1:
            flag = 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                s.append([nx, ny])
                maps[nx][ny] = maps[x][y] + 1
    answer = maps[n - 1][m - 1]
    if flag == 1:
        return answer - 1
    else:
        return -1


solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]])
