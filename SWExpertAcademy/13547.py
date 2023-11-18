tc = int(input())
for t in range(1, tc + 1):
    S = input()
    cnt = 0
    for s in S:
        if s == 'x':
            cnt += 1
    ans = 15 - cnt
    if ans >= 8:
        print("#{} {}".format(t, "YES"))
    else:
        print("#{} {}".format(t, "NO"))

