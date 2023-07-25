import sys

read = sys.stdin.readline

n, m = map(int, read().split())
A = list(map(int, read().split()))
B = list(map(int, read().split()))

ans = []
A_set = set(A)
B_set = set(B)

ans = list(A_set - B_set)
print(len(ans))
print(*ans)
# for a in A:
#     st = 0
#     en = len(B) - 1
#     while st <= en:
#         mid = (st + en) // 2
#         if a == B[mid]:
#             ans.append(a)
#             break
#         elif a < B[mid]:
#             en = mid - 1
#         elif a > B[mid]:
#             st = mid + 1
#
# if ans:
#     print(len(A) - len(ans))
#     for i in A:
#         if i not in ans:
#             print(i, end=" ")
# else:
#     print(0)
