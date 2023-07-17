t, w = map(int, input().split())
a = [0]
for i in range(t):
    a.append(int(input()))

d = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(t + 1):
    if a[i] == 1:
        d[i][0] = d[i - 1][0] + 1
    else:
        d[i][0] = d[i - 1][0]

    for j in range(1, w + 1):
        if a[i] == 2 and j % 2 == 1:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1]) + 1
        elif a[i] == 1 and j % 2 == 0:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1]) + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1])

print(max(d[t]))
