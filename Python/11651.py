#11651번 좌표 정렬하기2
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    xy = list(map(int, input().split()))
    arr.append([xy[1],xy[0]])
    
arr.sort()

for i in arr:
    print(i[1], i[0])
