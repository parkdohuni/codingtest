n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a = sorted(a)
for target in b:
    ans = 0
    st = 0
    en = n - 1
    while st <= en:
        mid = (st + en) // 2
        if target == a[mid] or target == a[st] or target == a[en]:
            ans = 1
            break
        elif target < a[mid]:
            en = mid - 1
        elif target > a[mid]:
            st = mid + 1
    print(ans)
