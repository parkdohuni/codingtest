# import sys
# N = int(input())
#
# schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
#
# dp = [0 for i in range(N+1)]
#
# for i in range(N):
#     for j in range(i+schedule[i][0], N+1):
#         if dp[j] < dp[i] + schedule[i][1]:
#             dp[j] = dp[i] + schedule[i][1]
#
# print(dp[-1])

# 퇴사 DP
n = int(input())
T = [0 for _ in range(n + 1)]
P = [0 for _ in range(n + 1)]
for i in range(n):
    x, y = map(int, input().split())
    T[i] = x
    P[i] = y
dp = [0 for i in range(n + 1)]
for i in range(len(T) - 2, -1, -1):
    # 최대 날짜 보다 작으면
    if i + T[i] <= n:
        dp[i] = max(dp[i + 1], dp[i + T[i]] + P[i])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
