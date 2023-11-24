import sys

input = sys.stdin.readline

original = input().rstrip()
bomb = input().rstrip()
stack = []
last_char = bomb[-1]
for char in original:
    stack.append(char)

    if char == last_char and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]


result = ''.join(stack)

if result:
    print(result)
else:
    print("FRULA")