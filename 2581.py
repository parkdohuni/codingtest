import sys
#m 60 n 100

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False  #소수 아님
    return True  #소수 맞음

m = int(input())
n = int(input())
sum = 0
index = 1
noprime = 0
for i in range(n - m + 1):
    if m + i != 1:
        if isPrime(m + i):
            sum += (m + i)
            noprime += 1
            if index == 1:
                min = m + i
                index = 0
    
if noprime == 0:
    print(-1)
else:
    print(sum)
    print(min)

