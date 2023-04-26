import sys

n = int(sys.stdin.readline())

val = 1
arr = []
ans = ''
for _ in range(n):
    k = int(sys.stdin.readline())
    
    while val <= k:
        arr.append(val)
        val += 1
        ans += '+\n'
        
    if arr[-1] == k:
        arr.pop()
        ans += '-\n'
    else:
        ans = 'NO'
        break
print(ans)
#     if val == 0:
#         val = 1
#         for _ in range(k):
#             arr.append(val)
#             val += 1
#             ans.append("+")
#     elif len(arr) == 0:
#         while(val <= k):
#             arr.append(val)
#             val += 1
#             ans.append("+")
        
#     if val == k:
#         arr.append(k)
#         ans.append("+")
#         arr.pop()
#         ans.append("-")
#     elif val > k:
#         temp = arr.pop()
#         if k != temp:
#             flag = 1
#             break
#         ans.append("-")
#     elif val < k:
#         while(val <= k):
#             arr.append(val)
#             val += 1
#             ans.append("+")
#         arr.pop()
#         ans.append("-")

# if flag == 0:
#     print("\n".join(ans))
# else:
#     print("NO")
    