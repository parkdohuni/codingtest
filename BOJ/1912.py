n = int(input())

d = list(map(int, input().split()))
save = 0
for i in range(n - 1):
    if d[i] + d[i + 1] >= d[i + 1]:
        d[i + 1] += d[i]
    else:
      continue

print(max(d))