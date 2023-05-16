for test_case in range(10):
    t = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for _ in range(t):
        high = arr.index(max(arr))
        low = arr.index(min(arr))
        if arr[high] == arr[low]:
            break
        arr[high] -= 1
        arr[low] += 1

    ans = max(arr) - min(arr)

    print("#{} {}".format(test_case + 1, ans))
