import sys

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())

    dp = [0] * (money + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(money + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    print(dp[money])