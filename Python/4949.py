import sys


while(1):
    str = sys.stdin.readline().rstrip()
    if str == '.':
        break
    stack = []
    check = 0
    
    for i in str:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack.pop() == '(':
                    check = 0
                else:
                    check = 1
                    break
            else:
                check = 1
                break

        elif i == ']':
            if stack:
                if stack.pop() == '[':
                    check = 0
                else:
                    check = 1
                    break
            else:
                check = 1
                break
    
    if stack or check == 1:
        print("no")
    else:
        print("yes")
        