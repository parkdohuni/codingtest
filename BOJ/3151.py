import sys

read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
arr = sorted(arr)
ans = 0
for i in range(n - 2):
    left = i + 1
    right = n - 1
    goal = -arr[i]
    idx = n
    while left < right:
        sum_ = arr[left] + arr[right]
        if sum_ < goal:
            left += 1
        elif sum_ == goal:
            if arr[left] == arr[right]:
                ans += right - left
            else:
                if idx > right:
                    idx = right
                    while idx >= 0 and arr[idx - 1] == arr[right]:
                        idx -= 1
                ans += right - idx + 1
            left += 1
        else:
            right -= 1
print(ans)
