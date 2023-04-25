import sys

n = int(sys.stdin.readline())


for _ in range(n):
    arr = input()
    left = []
    right = []
    for i in arr:
        if i == ">":
            if right:
                left.append(right.pop())
        elif i == "<":
            if left:
                right.append(left.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    print("".join(left)+"".join(reversed(right)))
            
