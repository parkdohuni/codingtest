s = int(input())
n = 1
while 1:
    if s < (n * (n + 1)) // 2:
        break
    else:
        n += 1

print(n - 1)