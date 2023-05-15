for test_case in range(10):
    building = int(input())
    ans = 0
    arr = list(map(int, input().split()))
    for i in range(2, building - 2):
        left = max(arr[i - 2], arr[i - 1])
        right = max(arr[i + 1], arr[i + 2])
        temp = arr[i] - max(left, right)
        if temp > 0:
            ans += temp
    print("#{} {}".format(test_case + 1, ans))
