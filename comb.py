import sys

n = int(input())
count = 1
a = 1
while(n > a):
    a = count * 6 + a
    count = count + 1
print(count)