#10816번 x보다 작은 수
import sys
input = sys.stdin.readline

n ,x = map(int, input().split())

arr = list(map(int, input().split()))
  
for i in range(n):
    if arr[i] < x:
        print(arr[i], end=" ")