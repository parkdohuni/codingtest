import math
import sys

def isPrime(n) :
    if n == 1:
        return False
    if n == 2 :
        return True

    if n % 2 == 0 :
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False

    return True

m, n = map(int, input().split())

for i in range(m , n + 1):
    if isPrime(i):
        print(i)