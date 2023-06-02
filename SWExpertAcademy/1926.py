t = int(input())
ans = []
for i in range(1, t + 1):
    res = ''
    n = i
    while n:
        a = int(n % 10)
        if a % 3 == 0 and a != 0:
            res += '-'
        n = int(n / 10)

    if len(res) == 0:
        ans.append(str(i))
    else:
        ans.append(res)

print(" ".join(ans))