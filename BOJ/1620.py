import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for i in range(1, n + 1):
    name = str(input().rstrip())
    dic[name] = i
    dic[i] = name

for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(dic[int(q)])
    else:
        print(dic[q])