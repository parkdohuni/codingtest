import sys

read = sys.stdin.readline

S1, S2 = read().strip(), read().strip()
l1, l2 = len(S1), len(S2)

dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if S1[i - 1] == S2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[l1][l2])
