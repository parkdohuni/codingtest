import sys

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        x = h
        y = int(n / h)
    else:
        x = n % h
        y = int(n / h) + 1
    y = '{0:02d}'.format(y)
    print(str(x)+str(y))