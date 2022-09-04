#10815번 숫자 카드
import sys

n = int(sys.stdin.readline())
narr = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
marr = list(map(int,sys.stdin.readline().split()))

dic = {}
for i in range(len(narr)):
    dic[narr[i]] = 0

for j in range(m):
    if marr[j] not in dic:
        print(0, end = ' ')
    else:
        print(1, end = ' ')