#1919번 애너그램 만들기
import sys
# input = sys.stdin.readline

# a = input().rstrip()
# b = input().rstrip()
# ans = 0

# a = sorted(a)
# b = sorted(b)

a = [0]*26
b = a[:]
ans = 0

for i in input():
    a[ord(i)-97] += 1
for i in input():
    b[ord(i)-97] += 1
for i in range(26):
    ans += abs(a[i]-b[i])
print(ans)