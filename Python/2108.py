#2108번 통계학
from collections import Counter
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

print(round(sum(arr)/n))

print(arr[n//2])

mode = Counter(arr).most_common()
if len(arr) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])

print(arr[-1] - arr[0])