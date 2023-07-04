n = int(input())

d = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        d[1] = 1
    elif i == 2:
        d[2] = 3
    else:
        d[i] = d[i - 2] * 2 + d[i - 1]

print(d[n] % 10007)
