n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max = 0
save = 0
ans = 0

for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            ans += 1

for x in range(n):
    for y in range(m):
        if arr[x][y] == 1:
            for k in range(4):
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                temp = 0
                nx = x
                ny = y
                while 1:
                    nx += dx[k]
                    ny += dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] == 6:
                            break
                        else:
                            temp += 1
                            if temp > max:
                                max = temp
                                save = k
                    else:
                        break
            nx = x
            ny = y
            while 1:
                nx += dx[save]
                ny += dy[save]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 6:
                        break
                    arr[nx][ny] = "#"
                    ans -= 1
                else:
                    break
        elif arr[x][y] == 2:
            for k in range(2):
                flag = 0
                temp = 0
                nx = 0
                ny = 0
                if k == 0:
                    for i in range(n):
                        if arr[i][y] == 2:
                            flag = 1
                        if arr[i][y] == 6 and flag == 1:
                            break
                        elif arr[i][y] == 6 and flag == 0:
                            ny = i
                        if arr[i][y] == 0:
                            temp += 1
                    if temp > max:
                        max = temp
                        save = k
                else:
                    for i in range(m):
                        if arr[x][i] == 2:
                            flag = 1
                        if arr[x][i] == 6 and flag == 1:
                            break
                        elif arr[x][i] == 6 and flag == 0:
                            nx = i
                        if arr[x][i] == 0:
                            temp += 1
                    if temp > max:
                        max = temp
                        save = k
            flag = 0
            if save == 0:
                for i in range(ny, n):

                    if arr[i][y] == 2:
                        flag = 1
                    if arr[i][y] == 6 and flag == 1:
                        break
                    if arr[i][y] == 0:
                        arr[i][y] = "#"
                        ans -= 1
            else:
                for i in range(nx, m):

                    if arr[x][i] == 2:
                        flag = 1
                    if arr[x][i] == 6 and flag == 1:
                        break
                    if arr[x][i] == 0:
                        arr[x][i] = "#"
                        ans -= 1
        # elif arr[x][y] == 3:

        elif arr[x][y] == 4:
            for k in range(4):
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                temp = 0
                nx = x
                ny = y
                while 1:
                    nx += dx[k]
                    ny += dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] == 6:
                            break
                        else:
                            temp += 1
                            if temp > max:
                                max = temp
                                save = k
                    else:
                        break
            nx = x
            ny = y
            while 1:
                nx += dx[save]
                ny += dy[save]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 6:
                        break
                    arr[nx][ny] = "#"
                    ans -= 1
                else:
                    break

        elif arr[x][y] == 5:
            nx = 0
            ny = 0
            for i in range(n):
                if arr[i][y] == 5:
                    flag = 1
                if arr[i][y] == 6 and flag == 1:
                    break
                elif arr[i][y] == 6 and flag == 0:
                    ny = i

            for i in range(m):
                if arr[x][i] == 5:
                    flag = 1
                if arr[x][i] == 6 and flag == 1:
                    break
                elif arr[x][i] == 6 and flag == 0:
                    nx = i

            for i in range(ny, n):
                if arr[i][y] == 5:
                    flag = 1
                if arr[i][y] == 6 and flag == 1:
                    break
                if arr[i][y] == 0:
                    arr[i][y] = "#"
                    ans -= 1

            for i in range(nx, m):
                if arr[x][i] == 5:
                    flag = 1
                if arr[x][i] == 6 and flag == 1:
                    break
                if arr[x][i] == 0:
                    arr[x][i] = "#"
                    ans -= 1


print(ans)
