#2577번 숫자의 개수
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
multi = a*b*c
ans = [0]*10
# print(multi)
while(1):
    save = int(multi % 10)
    ans[save] += 1
    multi = int(multi / 10)
    if(multi == 0):
        break
for i in ans:
    print(i, end="\n")