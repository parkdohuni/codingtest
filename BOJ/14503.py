import sys
from collections import deque

input = sys.stdin.readline


def clean_room():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    def turn_left():
        nonlocal d
        d = (d - 1) % 4

    graph = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1
    graph[r][c] = 2
    while True:
        cleaned = False
        for _ in range(4):
            turn_left()
            nx = dx[d] + r
            ny = dy[d] + c
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                r, c = nx, ny
                graph[r][c] = 2
                cnt += 1
                cleaned = True
                break

        if not cleaned:
            nx, ny = r - dx[d], c - dy[d]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
                r, c = nx, ny
            else:
                break
    print(cnt)

clean_room()