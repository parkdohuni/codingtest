#11659번 구간 합구하기4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
sum = [0]
total = 0

for i in range(len(arr)):
    total += arr[i]
    sum.append(total)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i - 1])
