#2559번 수열

# import sys
# input = sys.stdin.readline

# n, k = map(int,input().split())
# ans = [0] * (n-k+1)
# arr = list(map(int, input().split()))
# for i in range(n-k+1):
#     for j in range(k):
#         ans[i] = arr[i+j] + ans[i]
        
# print(max(ans))
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int, input().split()))

window_sum = sum(arr[:k]) # 첫 번째 윈도우의 합 계산
print(window_sum)
max_sum = window_sum

for i in range(1, n-k+1):
    # 이전 윈도우에서 제외되는 원소와 새로운 원소 계산하여 합 갱신
    window_sum = window_sum - arr[i-1] + arr[i+k-1] 
    max_sum = max(max_sum, window_sum)

print(max_sum)