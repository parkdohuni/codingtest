import sys
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