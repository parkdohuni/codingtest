import sys
input = sys.stdin.readline

arr = []
save = [0]*101

arr = list(map(int, input().split()))
for i in arr:
    save[i] += 1
flag = 0
print(save)
for j in arr:
    find = 100 - j
    if(save[find] > 0):
        flag = 1
        break
    else:
        continue

if(flag == 1):
    print(1)
else:
    print(0)

