#2751번 수 정렬하기2
import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
    
for i in sorted(arr):
    sys.stdout.write(str(i)+'\n')