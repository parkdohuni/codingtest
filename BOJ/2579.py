n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0] * n
    
if n < 3:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 3] + s[i] + s[i - 1], dp[i - 2] + s[i])
    print(dp[-1])
    
#     1. 첫 번째 계단

# DP[0] = stair[0]


# 2. 두 번째 계단

# DP[1] = stair[0] + stair[1]


# 3. 세 번째 계단

# DP[2] = stair[1] + stair[2] 혹은 stair[0] + stair[2]


# 둘 중 큰 값을 고릅니다.


# 4. 네 번째 계단

# DP[4] = stair[0] + stair[1] + stair[3] + stair[4] 혹은 stair[0] + stair[2] + stair[4]
# DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2] + stair[i])

