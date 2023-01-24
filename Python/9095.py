#9095번 1, 2, 3 더하기
import sys
input = sys.stdin.readline
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        d = [0] * (n + 1)
        d[1] = 1
        d[2] = 2
        d[3] = 4
        for i in range(4, n + 1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
        return d[n]
    
t = int(input())
for _ in range(t):
    n = int(input())
    print(sol(n))
    
    