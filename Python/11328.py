#11328번 애너그램 만들기
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    if len(a) != len(b):
        print("Impossible")
        continue
    if a == b:
        print("Possible")
    else:
        print("Impossible")
    