#13300번 방 배정
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0
girl = [0]*7
man = [0]*7

for _ in range(n):
    s, y = map(int, input().split())
    if s == 0:
        girl[y] += 1
    elif s == 1:
        man[y] += 1
    
for idx in range(0,7):
    if k < girl[idx]:
        ans += int((girl[idx] - 1) / k) + 1
        continue
           
    if girl[idx] > 0:
        ans += 1

for idx in range(0,7):
    if k < man[idx]:
        ans += int((man[idx] - 1) / k) + 1
        continue
        
    if man[idx] > 0:
        ans += 1
        
print(ans)