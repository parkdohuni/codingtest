import sys

read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))

left = 0
right = 0
ans = 0
temp = [False] * 100001
while right < n:
    if not temp[arr[right]]:# False 이면
        temp[arr[right]] = True
        right += 1
        ans += (right - left)
    else:
        temp[arr[left]] = False
        left += 1
print(ans)
