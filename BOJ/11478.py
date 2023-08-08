import sys
read = sys.stdin.readline

s = str(read().rstrip())

arr = []
for i in range(len(s)):
    for j in range(len(s) - i):
        arr.append(s[j:j + i + 1])

print(len(set(arr)))