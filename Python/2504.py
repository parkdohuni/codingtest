import sys

str = sys.stdin.readline().rstrip()
stack = []
x = 1
ans = 0

for i in range(len(str)):
    if str[i] == "(":
        stack.append(str[i])
        x *= 2
    
    elif str[i] == "[":
        stack.append(str[i])
        x *= 3
        
    elif str[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if str[i-1] == "(":
            ans += x
        stack.pop()
        x //= 2
        
    elif str[i] == "]":
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if str[i-1] == "[":
            ans += x
        stack.pop()
        x //= 3
        
if stack:
    print(0)
else:
    print(ans)
       