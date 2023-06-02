# from collections import deque
# t = int(input())
#
# for test_case in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     big = max(arr)
#     cnt = 1
#     ans = 0
#     stack = deque()
#     for i in range(len(arr)):
#         if big == arr[i]:
#             while stack:
#                 ans += big - stack.popleft()
#             if i != len(arr)-1:
#                 big = max(arr[i+1:])
#             continue
#         stack.append(arr[i])
#         cnt += 1
#
#
#     print("#{} {}".format(test_case + 1, ans))

t = int(input())

for test_case in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    ans = 0
    big = arr[0]
    for i in range(len(arr)):
        if big < arr[i]:
            big = arr[i]
            continue
        else:
            ans += big - arr[i]
    print("#{} {}".format(test_case + 1, ans))

