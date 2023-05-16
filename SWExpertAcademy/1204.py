t = int(input())

for _ in range(1, t+1):
    test_case = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    cnt = [0] * 101
    for i in range(len(arr)):
        cnt[arr[i]] += 1
    cnt.reverse()
    ans = cnt.index(max(cnt))
    ans = 100 - ans
    print("#{} {}".format(test_case, ans))