#14425번 문자열 집합
import sys
input = sys.stdin.readline
n ,m = map(int, input().split())

s = set([input() for _ in range(n)])

cnt = 0
for _ in range(m):
    t = input()
    if t in s:
        cnt += 1
print(cnt)