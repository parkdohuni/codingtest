import sys

n = int(sys.stdin.readline())
ans = 0
for _ in range(n):
    str = sys.stdin.readline().rstrip()
    stack = []

    for i in range(len(str)):
        
        if not stack:
            if str[i] == 'A':
                stack.append(str[i])
                
            elif str[i] == 'B':
                stack.append(str[i])
        else:
            if str[i] == 'A':
                if stack[-1] == 'A':
                    stack.pop()
                else:
                    stack.append(str[i])
            if str[i] == 'B':
                if stack[-1] == 'B':
                    stack.pop()
                else:
                    stack.append(str[i])
    
    if not stack:
        ans += 1
print(ans)
        