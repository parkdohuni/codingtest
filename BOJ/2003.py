import sys

read = sys.stdin.readline

n, m = map(int, read().split())
arr = list(map(int, read().split()))
ans = 0
left = 0
right = 0
sum_ = 0
while right <= n:
    if m == sum_:
        ans += 1
        sum_ -= arr[left]
        left += 1
    elif m < sum_:
        sum_ -= arr[left]
        left += 1
    elif m > sum_:
        if right == n:
            break
        sum_ += arr[right]
        right += 1
print(ans)