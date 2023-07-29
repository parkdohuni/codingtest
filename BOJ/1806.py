import sys

read = sys.stdin.readline
n, s = map(int, read().split())
left = 0
right = 0
arr = list(map(int, read().split()))
ans = 100001
temp = arr[left]
# s < 가장 짧은 것
while left < n:
    if s <= temp:
        ans = min(ans, right - left + 1)
        temp -= arr[left]
        left += 1
    else:
        right += 1
        if right >= n:
            break
        temp += arr[right]

print(0) if ans == 100001 else print(ans)