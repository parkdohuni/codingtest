t = int(input())

for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    d = [[0] * (len(coin) + 1) for _ in range(1)]
    for i in range(len(coin)):
        if m % coin[i] == 0:
            d[0][i] = m // coin[i]
            break
        else:
           temp = m // coin[i]
           m = m - temp * coin[i]

    