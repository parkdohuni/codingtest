from itertools import combinations
import sys

input = sys.stdin.readline

L, C = map(int, input().split())

alpha = list(input().split())
result = list(combinations(alpha, L))
vowel = ['a', 'e', 'i', 'o', 'u']
ans = []
for i in result:
    i = list(i)
    i.sort()
    cnt = 0
    for j in vowel:
        if j in i:
            cnt += 1
    if 1 <= cnt <= L - 2:
        ret = ''.join(i)
        ans.append(ret)
ans.sort()
print(*ans)
