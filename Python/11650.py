#11650번 좌표 정렬하기
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    xy = list(map(int, input().split()))
    arr.append(xy)
    
arr.sort()
for i in arr:
    print(i[0], i[1])
