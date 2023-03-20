#11047번 동전 0
import sys
input = sys.stdin.readline

n ,k = map(int, input().split())
#n 동전의 종류, k 그 가치의 합
#필요한 동전의 개수의 최솟값
arr = []

for i in range(n):
    arr.append(int(input()))

len = -1
ans = 0
for i in range(n):
    max_val = arr[len]
    len -= 1
    if(k >= max_val):
        temp = int(k) // int(max_val)
        ans += temp
        k = k % max_val
    else:
        continue

print(ans)