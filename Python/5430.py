import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(x)
    rev = 0
    flag = 0
    if n == 0:
        queue = []
    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(queue) == 0:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
                    
    if flag == 0:
        if rev % 2 == 0:
            print("["+",".join(queue) + "]")
        else:
            queue.reverse()
            print("["+",".join(queue) + "]")
        