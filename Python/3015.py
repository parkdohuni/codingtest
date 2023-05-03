import sys

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    
stack = []
ans = 0
for i in arr:
    #i번째 사람 키가 더 클 때
    while stack and stack[-1][0] < i:
        ans += stack.pop()[1]
        
    if not stack:
        stack.append([i, 1])
        continue
    #키가 같을 때
    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        ans += cnt
        
        if stack: ans += 1
        stack.append((i, cnt + 1))
    #키가 작을 때
    else:
        stack.append((i, 1))
        ans += 1

print(ans)