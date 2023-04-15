#3273번 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

left = 0
right = n - 1
ans = 0
a.sort()

while(1):
    if right == left:
        break
    temp = a[left] + a[right]
    if temp == x:
        ans += 1
    if temp < x:
        left += 1
    else:
        right -= 1

print(ans)