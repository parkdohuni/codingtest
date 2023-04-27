import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
    
stack = []
ans = 0

for i in arr:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    
    ans += len(stack) - 1
    
print(ans)
