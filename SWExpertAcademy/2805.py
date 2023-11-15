t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    ans = 0
    arr = [list(map(int, input())) for _ in range(n)]
    mid = n // 2
    st = mid
    en = mid + 1
    for i in range(n):
        ans += sum(arr[i][st:en])
        if i < mid:
            st -= 1
            en += 1
        else:
            st += 1
            en -= 1
    print("#{} {}".format(tc, ans))
