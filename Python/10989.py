#10989번 수 정렬하기3
import sys

n = int(sys.stdin.readline())
num = [0] * 10001

for _ in range(n):
    input_num = int(sys.stdin.readline())
    num[input_num] += 1
    
for i in range(10001):
    if num[i] > 0:
        for j in range(num[i]):
            print(i)