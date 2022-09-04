#10816번 숫자 카드2
import sys
input = sys.stdin.readline

n = int(input())

narr = list(map(int,input().split()))
snarr = list(set(narr))

m = int(input())
marr = list(map(int,input().split()))

dic = {}
for i in narr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
for i in range(m):
    if marr[i] in dic:
        print(dic.get(marr[i]), end = ' ')
    else:
        print(0, end=' ')
        