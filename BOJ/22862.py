import sys
read = sys.stdin.readline
n, k = map(int, read().split())
arr = list(map(int, read().split()))

left = 0
right = 0
ans = 0
cnt = 0
even = 0
for start in range(n):
    while cnt <= k and right < n:
        if arr[right] % 2 == 0:
            even += 1
        else:
            cnt += 1
        right += 1

        if start == 0 and right == n:
            ans = even
            break

    if cnt == k + 1:
        ans = max(even, ans)

    if arr[start] % 2 == 0:
        even -= 1
    else:
        cnt -= 1
print(ans)
















# N, K = map(int, input().split())
# S = list(map(int, input().split()))
#
# end = 0  # 끝 포인터
# result = 0  # 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이(출력값)
# tmp = 0  # 현재 짝수 부분 수열의 길이
# count = 0  # 지우려는 홀수 카운트
#
# # start를 N 까지 계속 증가시키며 반복
# for start in range(N):
#
#     # end를 가능한 만큼 이동
#     while (count <= K and end < N):
#
#         if S[end] % 2 == 1:  # 홀수
#             count += 1
#         else:  # 짝수
#             tmp += 1
#         end += 1  # 끝 점 이동
#
#         if start == 0 and end == N:
#             result = tmp
#             break
#
#     if count == K + 1:
#         result = max(tmp, result)
#
#     if S[start] % 2 == 1:  # 시작점이 홀수
#         count -= 1
#     else:  # 시작점이 짝수
#         tmp -= 1
#
# print(result)