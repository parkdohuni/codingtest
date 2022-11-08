import sys
a, b, c = map(int, input().split())
count = 0
if b < c:
    n = int(a/(c - b))
    print(n+1) 
else:
    print(-1)       
    