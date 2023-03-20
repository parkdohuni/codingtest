#11399번 ATM
import sys
input = sys.stdin.readline

n = int(input())
ans = 0
arr = list(map(int, input().split()))
arr = sorted(arr)
for i in range(n):
    ans += arr[i] * (n)
    n -= 1
    

print(ans)