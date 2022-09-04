import sys

n = int(input())
result = 0
for i in range(1, n+1):
    arr = list(map(int, str(i)))
    result = i + sum(arr)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)