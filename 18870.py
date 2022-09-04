#18870번 좌표 압축
import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
sarr = []

sarr = list(sorted(set(arr)))

dic = {sarr[i]:i for i in range(len(sarr))}

for i in arr:
    print(dic[i],end=' ')