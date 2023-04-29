import sys

n  = int(sys.stdin.readline())
queue = []
for i in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    
    if cmd[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
        
    if cmd[0] == "size":
        print(len(queue))
    
    if cmd[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    if cmd[0] == "front":
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue[0])
            
    if cmd[0] == "back":
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue[-1])
            