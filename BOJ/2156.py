n = int(input())

a = [0] + [int(input()) for _ in range(n)] + [0]
d = [0] * (n + 2)

d[1] = a[1]
d[2] = d[1] + a[2]

for i in range(3, n + 1):
    d[i] = max(a[i] + a[i - 1] + d[i - 3], a[i] + d[i - 2], d[i - 1])

print(d[n])
