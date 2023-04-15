#10807번 개수 세기
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
v = int(input())
ans = 0
for i in a:
    if v == i:
        ans += 1
        
print(ans)