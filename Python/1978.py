import sys

n = int(input())
prime = [int(n) for n in input().strip().split()]
cnt = 0
flag = 0
for i in range(n):
    if prime[i] != 1:
        for x in range(2, prime[i]):
            if prime[i] % x == 0:
                flag = 1
        if flag == 0:
            cnt += 1
    flag = 0
print(cnt)