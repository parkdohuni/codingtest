#10814번 나이순 정렬
from posixpath import split
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    age, name = input().split()
    arr.append([int(age), name])

arr.sort(key=lambda x:int(x[0]))
#람다 함수를 이용해 첫번째 요소에 대해서만 정렬
for i in arr:
    print(i[0], i[1])
