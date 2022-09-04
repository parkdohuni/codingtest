import sys


import sys

n = int(input())
sum = 0
cnt = 1
x = 1
while(1):
    sum = sum + cnt
    if(n <= sum):
        key = n - (sum - cnt)
        break
    cnt = cnt + 1
if(cnt % 2 == 0):
    print(str(key) + "/" + str(cnt+1-key))
else:
    print(str(cnt+1-key) + "/" + str(key))