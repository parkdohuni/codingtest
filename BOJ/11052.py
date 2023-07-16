n = int(input())
a = [0] + list(map(int, input().split()))

d = [0] * (n + 1)
d[1] = a[1]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        d[i] = max(a[j] + d[i-j], d[i])
print(d[n])