import sys

read = sys.stdin.readline

n, m = map(int, read().split())
A = set(map(int, read().split()))
B = set(map(int, read().split()))

ans = A - B
ans = sorted(ans)
print(len(ans))
if len(ans) !=0:
    print(*(ans))
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
