t = int(input())

for tc in range(1, t + 1):
    ans = 0
    arr = list(map(int, input().split()))
    arr.sort()
    ans = (sum(arr) - arr[0] - arr[-1]) / 8
    print("#{} {}".format(tc, round(ans)))
