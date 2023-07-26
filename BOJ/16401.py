import sys

read = sys.stdin.readline

m, n = map(int, read().split())

arr = list(map(int, read().split()))
start = 1
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    if mid == 0:
        total = 0
        break

    for x in arr:
        if x >= mid:
            total += (x // mid)

    if total >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
