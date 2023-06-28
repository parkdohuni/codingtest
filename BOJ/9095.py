n = int(input())

for _ in range(n):
    tc = int(input())

    if tc == 1:
        print(1)
        continue
    elif tc == 2:
        print(2)
        continue
    elif tc == 3:
        print(4)
        continue
    else:
        d = [0] * (tc + 1)
        d[1] = 1
        d[2] = 2
        d[3] = 4
    for i in range(4, tc + 1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[tc])