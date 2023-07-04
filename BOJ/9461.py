n = int(input())

for _ in range(n):
    t = int(input())
    d = [0] * (t + 1)
    for i in range(1, t + 1):
        if i == 1:
            d[1] = 1
        elif i == 2:
            d[2] = 1
        elif i == 3:
            d[3] = 1
        elif i == 4:
            d[4] = 2
        else:
            d[i] = d[i - 1] + d[i - 5]
    print(d[t])
