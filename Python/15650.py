#15650번 N과 M(2)

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
s = []
visited = [False] * (n+1)

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)