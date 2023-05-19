t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    big = 0
    sum = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for r in range(i, m + i):
                for c in range(j, m + j):
                    sum += arr[r][c]
            if sum > big:
                big = sum
    print("#{} {}".format(tc, big))