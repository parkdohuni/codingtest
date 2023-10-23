from collections import deque


def solution(board):
    q = deque()
    x_max = len(board[0])
    y_max = len(board)
    visited = [[-1 for _ in range(x_max)] for _ in range(y_max)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    def move(x, y, i):
        while True:
            x += dx[i]
            y += dy[i]
            if x < 0 or y < 0 or x >= x_max or y >= y_max:
                break
            if board[y][x] == 'D':
                break
        return y - dy[i], x - dx[i]

    for i in range(y_max):
        for j in range(x_max):
            if board[i][j] == "R":
                q.append([i, j])
                visited[i][j] = 0
            if board[i][j] == "G":
                x_goal = j
                y_goal = i

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = move(x, y, i)
            if visited[ny][nx] == -1:
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

    return visited[y_goal][x_goal]


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# print(solution([".D.R", "....", ".G..", "...D"]	))
