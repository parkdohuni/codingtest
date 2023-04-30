import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

ans = 0
queue = deque([i for i in range(1, n+1)])
arr = list(map(int, sys.stdin.readline().split()))
for i in arr:
    
    while(1):
        if queue[0] == i:
            queue.popleft()
            break
        
        if queue.index(i) <= len(queue)//2:
            queue.rotate(-1)
            ans += 1
        else:
            queue.rotate(1)
            ans += 1
            

print(ans)
    