#1181번 단어 정렬
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    word = input()
    arr.append([len(word), word])
arr.sort()
pre_print = ''
for i in range(len(arr)):
    if pre_print != arr[i][1]:
        print(arr[i][1])
    pre_print = arr[i][1]