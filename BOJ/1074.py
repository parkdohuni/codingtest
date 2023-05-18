n, r, c = map(int, input().split())


# n이 1일 때 탐색한다?

def zz(n, r, c):
    if n == 0:
        return 0
    else:
        half = 2 ** (n - 1)
        if r < half and c < half:
            return zz(n - 1, r, c)
        if r < half <= c:
            return half * half + zz(n - 1, r, c - half)
        if r > half > c:
            return 2 * half * half + zz(n - 1, r - half, c)


print(zz(n, c, r))
