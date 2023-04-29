import sys
while(1):
    arr = list(map(int, sys.stdin.readline().split()))
    n = arr.pop(0)
    if n == 0:
        break
    left = []
    right = []
    for i in range(n):
        while left and left[-1] > arr[i]:
            left.append(arr[i])
        
        if not left:
            left.append(arr[i])
        
        if left[-1] < arr[i]:
            right.append(arr[i])
            
        if 
print(arr)