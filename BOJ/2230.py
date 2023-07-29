import sys

read = sys.stdin.readline

n, m = map(int, read().split())
arr = []
for _ in range(n):
    arr.append(int(read()))

arr = sorted(arr)
left = 0
right = 0
ans = float("INF")
while n > left:
    temp = arr[right] - arr[left]
    if m <= temp:
        if ans > temp:
            ans = temp
        left += 1
    else:
        right += 1
        if right >= n:
            break

print(ans)