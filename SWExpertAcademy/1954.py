t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = [[0 for j in range(n)] for i in range(n)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    x = y = 0
    idx = 0
    for num in range(1, n ** 2 + 1):
        arr[x][y] = num
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] != 0:
            idx = (idx + 1) % 4
            nx = x + dx[idx]
            ny = y + dy[idx]
        x = nx
        y = ny


    print("#{}".format(test_case))
    for ans in arr:
        print(*ans)