t = int(input())

for tc in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())
    ans = 0
    a = w * p
    b = q
    if w > r:
        b += (w - r) * s
    if a < b:
        ans = a
    else:
        ans = b
    print("#{} {}".format(tc, ans))
