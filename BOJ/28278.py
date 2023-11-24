import sys

input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    x = list(input().split())
    # print(x)
    command = int(x[0])
    if command == 1:
        stack.append(int(x[-1]))
    elif command == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif command == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)