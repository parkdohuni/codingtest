n = int(input())
m = int(input())
a = []
for _ in range(m):
    k = int(input())
    a.append(k)

d = [0] * (n + 1)
d[0] = 1
d[1] = 1
for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]
ans = 1
temp = 1
cnt = 0
for i in range(1, n + 1):
    cnt += 1
    if a.__contains__(i):
        temp = d[cnt - 1]
        ans *= temp

        cnt = 0
    elif i == n:
        temp = d[cnt]
        ans *= temp
print(ans)
