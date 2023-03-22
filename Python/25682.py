#25682번 체스판 다시 칠하기2

import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())
arr = [0 for _ in range(n)]
for i in range(n):    
	arr[i] = list(map(int, input().split()))