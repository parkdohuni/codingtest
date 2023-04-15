#1457번 방 번호
import sys
input = sys.stdin.readline

arr = [0] * 10
n = int(input())

while(1):
    save = int(n % 10)
    arr[save] += 1
    n = int(n / 10)
    # if(max < arr[save]):
    #     max = arr[save]
    if(n == 0):
        break

temp = arr[6] + arr[9]
if(int(temp % 2) == 0):
    arr[6] = int(temp/2)
    arr[9] = int(temp/2)
else:
    arr[6] = int(temp/2) + 1
    arr[9] = int(temp/2) + 1

print(max(arr))
