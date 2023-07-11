n = int(input())
arr = list(map(int, input().split()))
d = [0] * n
d[0] = 1

for i in range(n):
    for j in range(i):
        if i == j + 1:
            d[i] += 1
        if arr[i] > arr[j] :
            d[i] += 1
        temp = arr[j]

print(max(d))