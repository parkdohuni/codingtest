n = int(input())

dp = [[0 for i in range(n)] for _ in range(3)]

R = [0] * 3
G = [0] * 3
B = [0] * 3
dp[1][0] = R[0]
dp[1][1] = G[0]
dp[1][2] = B[0]
for i in range(2, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + R[1]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + G[1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + B[1]

print(min(dp[n][0], dp[n][1], dp[n][2]))
