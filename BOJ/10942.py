# n = int(input())
# arr = list(map(int, input().split()))
#
# m = int(input())
# for _ in range(m):
#     s, e = map(int, input().split())
#     num = (e - s + 1) // 2
#     ans = 1
#     for i in range(num):
#         if arr[s - 1 + i] == arr[e - 1 - i]:
#             ans = 1
#         else:
#             ans = 0
#             break
#     print(ans)
#
import sys

input = sys.stdin.readline

n = int(input())
a = list(input().split())
m = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if a[i] == a[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, n):
    for j in range(n-i):
        if a[j] == a[i + j] and dp[j + 1][i + j - 1] == 1:
            dp[j][i + j] = 1

for i in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
