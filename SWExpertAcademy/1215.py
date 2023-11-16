def check(x, y, n):
    cnt = 0
    mid = n // 2
    for i in range(mid):
        # print(y - i, y - n + 1 + i)
        # print(arr[x][y - i], arr[x][y - n + 1 + i])
        if arr[x][y - i] == arr[x][y - n + 1 + i]:
            cnt = 1
        else:
            return 0
    return cnt


def check_ver(x, y, n):
    cnt = 0
    mid = n // 2
    for i in range(mid):
        # print(x, y - i, y - n + 1 + i)
        # print(arr[y - i][x], arr[y - n + 1 + i][x])
        if arr[y - i][x] == arr[y - n + 1 + i][x]:
            cnt = 1
        else:
            return 0
    return cnt


for tc in range(1, 11):
    ans = 0
    n = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            x = i
            y = n + j - 1
            if y >= len(arr):
                break
            else:
                ans += check(x, y, n)
                ans += check_ver(x, y, n)
    print("#{} {}".format(tc, ans))