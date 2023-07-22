n = int(input())

d = [0] * 1001
ans = ["SK", "CY"]
d[2] = 1
for i in range(3, n + 1):
    d[i] = d[i - 2]

print(ans[d[n]])
