import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().strip().split()))
ans = []
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > arr[i]:
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, arr[i]])
    
print(" ".join(map(str, ans)))
