#2577번 숫자의 개수
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
multi = a*b*c
ans = [0]*10

while(1):
    save = multi % 10
    ans[save] += 1
    multi = multi / int(10)
    if(multi == 0):
        break
print(ans, end="\n")