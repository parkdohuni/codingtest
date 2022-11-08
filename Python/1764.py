#1764 듣보잡
import sys
input = input = sys.stdin.readline
n ,m = map(int, input().split())
heard = {}
cnt = 0
for i in range(n):
    word = input().rstrip()
    heard[word] = i
li = []
for j in range(m):
    seen = input().rstrip()
    if seen in heard:
        cnt += 1
        li.append(seen)
        
print(cnt)
li.sort()
for i in range(len(li)):
    print(li[i])
