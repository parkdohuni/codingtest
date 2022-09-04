import math
import sys

limit = 10000

primes = []
eratos = [False,False] + [True] * (limit - 1)

for i in range(2, limit+1):
    if eratos[i]:
        primes.append(i)
        for j in range(i + i, limit+1, i):
            eratos[j] = False

T = int(input())
for i in range(T):
    ans1 = 0
    ans2 = 0
    even = int(input())
    
    even_first = even//2
    
    ans1 = even_first
    ans2 = even_first
    
    if ans1 not in primes and ans2 not in primes:
        while True:
            ans1 -= 1
            ans2 += 1
            
            if ans1 in primes and ans2 in primes:
                break
            
    print("{0} {1}".format(ans1 ,ans2))