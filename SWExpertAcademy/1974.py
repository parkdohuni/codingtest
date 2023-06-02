t = int(input())

for tc in range(1, t + 1):
    ans = 1
    arr = [list(map(int, input().split())) for _ in range(9)]

    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(9):
                if arr[i][j] == arr[i][k] and k != j:
                    ans = 0
                    break
                if arr[i][j] == arr[k][j] and k != i:
                    ans = 0
                    break

            if i < 3:
                x = 3
            elif 3 <= i < 6:
                x = 6
            elif 6 <= i < 9:
                x = 9
            if j < 3:
                y = 3
            elif 3 <= j < 6:
                y = 6
            elif 6 <= j < 9:
                y = 9
            for dx in range(x - 3, x):
                for dy in range(y - 3, y):
                    if arr[i][j] == arr[dx][dy] and i != dx and j != dy:
                        ans = 0
                        break

    print("#{} {}".format(tc, ans))
