n = int(input())

d = [0] * (n + 2)
d[1] = 1
d[2] = 2
for i in range(1, n - 1):
    d[i + 2] = (d[i] + d[i + 1]) % 15746

print(d[n] % 15746)
