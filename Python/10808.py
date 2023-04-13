import sys
input = sys.stdin.readline
s = input()
lst = [0]*26
for i in s:
    lst[ord(i)-97]+=1
for i in lst:
    print(i,end= ' ')
#1.  아스키코드
#ord(문자) = 숫자 ; 문자를 숫자로 바꿔주는 함수
# ord('a') = 97 이기 때문에
# ord('a')-97로 0으로 만들어서 lst와 index를 맞춰준다.

# s = input()
# print(s)
# ans = [0]*26
# for i in s:
#     match i:
#         case "a":
#             ans[0] += 1
#         case "b":
#             ans[1] += 1
#         case "c":
#             ans[2] += 1
#         case "d":
#             ans[3] += 1
#         case "e":
#             ans[4] += 1
#         case "f":
#             ans[5] += 1
#         case "g":
#             ans[6] += 1
#         case "h":
#             ans[7] += 1
#         case "i":
#             ans[8] += 1
#         case "j":
#             ans[9] += 1
#         case "k":
#             ans[10] += 1
#         case "l":
#             ans[11] += 1
#         case "n":
#             ans[12] += 1
#         case "m":
#             ans[13] += 1
#         case "o":
#             ans[14] += 1
#         case "p":
#             ans[15] += 1
#         case "q":
#             ans[16] += 1
#         case "r":
#             ans[17] += 1
#         case "s":
#             ans[18] += 1
#         case "t":
#             ans[19] += 1
#         case "u":
#             ans[20] += 1
#         case "v":
#             ans[21] += 1
#         case "w":
#             ans[22] += 1
#         case "x":
#             ans[23] += 1
#         case "y":
#             ans[24] += 1
#         case "z":
#             ans[25] += 1
# print(ans)     
             