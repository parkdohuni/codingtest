import sys

a, b, v = map(int, input().split())
x = v - a
y = a - b
if a == v:
    print(1)
elif x < y:
    print(int(x / y) + 2)
elif x % y > 0:
    print(int(x / y) + 2)
else:
    print(int(x / y) + 1)

