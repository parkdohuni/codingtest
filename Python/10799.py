import sys

str = sys.stdin.readline().rstrip()
stack = []
ans = 0
temp = 1
for i in range(len(str)):
    if str[i] == '(':
        stack.append('(')
        
    elif str[i] == ')':
        stack.pop()
        if str[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1
            
print(ans)