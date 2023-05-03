import sys
from collections import deque
t = int(sys.stdin.readline())
flag = 0
for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(x)
    
    for i in p:
        if i == "R":
            queue.reverse()
        elif i == "D":
            if queue:
                queue.popleft()
            else:
                flag = 1
                
    if flag == 1:
        print("error")
    else:
        print(queue)