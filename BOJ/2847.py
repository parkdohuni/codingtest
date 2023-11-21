import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.reverse()
ans = 0
for i in range(len(arr) - 1):
    if arr[i] <= arr[i + 1]:
        dist = arr[i + 1] - arr[i] + 1
        ans += dist
        arr[i + 1] -= dist

print(ans)