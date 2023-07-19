# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     coin = list(map(int, input().split()))
#     m = int(input())
#     d = [[0] * (len(coin) + 1) for _ in range(100000)]
#     money = m
#     ans = 1
#     for i in range(len(coin) - 1, -1, -1):
#         temp = money // coin[i]
#         d[0][i] = temp
#         money = money - (temp * coin[i])
#     idx = 1
#     big = d[0][len(coin) - 1]
#     while big > 0:
#         big -= 1
#         flag = 0
#         money = m - big * coin[-1]
#         for i in range(len(coin) - 2, -1, -1):
#             if money % coin[i] == 0:
#                 d[idx][i] = money // coin[i]
#                 d[idx][len(coin) - 1] = big
#                 money -= d[idx][i] * coin[i]
#                 flag = 1
#         if flag == 1:
#             idx += 1
#             ans += 1
#     print(ans)
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    d = [0] * (m + 1)
    d[0] = 1

    for coin in coins:
        for i in range(m + 1):
            if i >= coin:
                d[i] += d[i - coin]

    print(d[m])
