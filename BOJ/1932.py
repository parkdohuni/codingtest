# n = int(input())
#
# d = [[0] * (n + 1) for _ in range(n + 1)]
# d = [list(map(int, input().split())) for _ in range(n)]
# d[1][0] += d[0][0]
# d[1][1] += d[0][0]
# for i in range(2, n):
#     for j in range(i + 1):
#         if j == 0:
#             d[i][j] += d[i - 1][0]
#         elif j == i:
#             d[i][j] += d[i - 1][j - 1]
#         else:
#             d[i][j] += max(d[i - 1][j], d[i - 1][j - 1])
#
# print(max(d[n-1]))
import sys

input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        dp[i][j] = max(dp[i][j] + dp[i + 1][j], dp[i][j] + dp[i + 1][j + 1])
print(dp[0][0])

