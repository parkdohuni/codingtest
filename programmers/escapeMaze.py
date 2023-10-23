from collections import deque


def solution(maps):
    def bfs(x, y):
        visited = [[0 for _ in range(x_max)] for _ in range(y_max)]
        q = deque()
        q.append(x)
        while q:
            qy, qx = q.popleft()
            for i in range(4):
                nx = dx[i] + qx
                ny = dy[i] + qy
                if 0 <= nx < x_max and 0 <= ny < y_max and not visited[ny][nx] and maps[ny][nx] != "X":
                    visited[ny][nx] = visited[qy][qx] + 1
                    q.append((ny, nx))

        return visited[y[0]][y[1]]

    x_max = len(maps[0])
    y_max = len(maps)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for iy in range(y_max):
        for ix in range(x_max):
            if maps[iy][ix] == 'S':
                start = (iy, ix)
            elif maps[iy][ix] == 'E':
                end = (iy, ix)
            elif maps[iy][ix] == 'L':
                lever = (iy, ix)
    distance1 = bfs(start, lever)
    distance2 = bfs(lever, end)

    return distance1 + distance2 if distance1 and distance2 else -1


# print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
# print(solution(["SELXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
