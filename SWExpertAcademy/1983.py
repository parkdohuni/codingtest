t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    for _ in range(n):
        a, b, c = map(int, input().split())
        total = a * 35 / 100 + b * 45 / 100 + c * 20 / 100

    ans = 0
    print("#{} {}".format(tc, ans))
