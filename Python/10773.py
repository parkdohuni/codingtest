import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if len(arr) != 0:
            arr.pop()
    else:
        arr.append(k)

print(sum(arr))
    