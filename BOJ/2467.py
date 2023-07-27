import sys

read = sys.stdin.readline

n = int(read())
liquids = list(map(int, read().split()))

ans = float("INF")
ans_left = 0
ans_right = 0

for i in range(n - 1):
    cur = liquids[i]
    st = i + 1
    en = n - 1
    while st <= en:
        mid = (st + en) // 2
        temp = cur + liquids[mid]

        if abs(temp) < ans:
            ans = abs(temp)
            ans_left = i
            ans_right = mid
            if ans == 0:
                break

        if temp < 0:
            st = mid + 1
        else:
            en = mid - 1

print(liquids[ans_left], liquids[ans_right])
