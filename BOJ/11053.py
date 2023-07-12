n = int(input())
arr = list(map(int, input().split()))
d = [1] * n
save = []
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            save.append(d[j])

    if save:
        d[i] = max(save) + 1
    save = []

print(max(d))
