tc = int(input())

for t in range(1, tc + 1):
    ans = 0
    result = []
    max_cnt = 0
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    temp = []
    for i in range(len(arr)):
        cnt = 0
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] <= K:
                cnt += 1
            else:
                break
        max_cnt = max(max_cnt, cnt)

    print("#{} {}".format(t, max_cnt + 1))
