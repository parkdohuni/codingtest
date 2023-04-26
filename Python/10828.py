import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif cmd == "size":
        print(len(arr))
    elif cmd == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "pop":        
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif "push" in cmd:
        arr.append(int(cmd[4:]))