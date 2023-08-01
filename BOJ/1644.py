import math
import sys

read = sys.stdin.readline

n = int(read())
prime = []
flag = 1
ans = 0
a = [False, False] + [True] * (n + 1)
for i in range(2, n + 1):
    if a[i]:
        prime.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

left = 0
right = 0
sum_ = 0
while left <= right <= len(prime):
    if sum_ == n:
        ans += 1
        sum_ -= prime[left]
        left += 1
    elif sum_ < n:
        if right == len(prime):
            break
        sum_ += prime[right]
        right += 1
    elif sum_ > n:
        sum_ -= prime[left]
        left += 1

print(ans)
