import sys

input = sys.stdin.readline

dp = [1, 2, 4, 7]
n = int(input())
for i in range(n):
    tc = int(input())
    for j in range(len(dp), tc):
        dp.append((dp[-3] + dp[-2] + dp[-1]) % 1000000009)
    print(dp[tc - 1])
