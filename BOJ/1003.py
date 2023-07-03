n = int(input())

for _ in range(n):
    t = int(input())
    d = [[0] * 2 for _ in range(t + 1)]

    if t == 0:
        d[0][0] = 1
        d[0][1] = 0
        print(' '.join(map(str, d[0])))
    elif t == 1:
        d[1][0] = 0
        d[1][1] = 1
        print(' '.join(map(str, d[1])))
    else:
        d[0][0] = 1
        d[0][1] = 0
        d[1][0] = 0
        d[1][1] = 1
        for i in range(2, t + 1):
            d[i][0] = d[i-1][0] + d[i-2][0]
            d[i][1] = d[i-1][1] + d[i-2][1]
        print(' '.join(map(str, d[t])))
