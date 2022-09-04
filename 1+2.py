import re
import sys

height = 172.5
a = '키는 %.2f 입니다.' %height
print(a)
print(a, end='123')
test = 'hello {}'.format('bob')
print(test)

year = 2020
month = 3
day = 5
b = '%d-%02d-%02d' %(year,month,day)
print(b)
print(year, month, day, sep='/')

def strReverse1(string):
    return string[::-1]

def strReverse(string):
    return reversed(string)

# in_string = input('문자열을 입력하세요: ')
# result = strReverse(in_string)
# print(''.join(result))

# name = input('이름을 입력하세요: ')
# print('%s님 반갑습니다.' %name)

input = sys.stdin.readline

score = 85
result = "Success" if score>=80 else "Fail"
print(result)

c = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]

a = 13
b = 99
a,b = b,a
print('a:{a}, b:{b}')

target = 1
arr = [1,2,5,1,1]
a = list(filter(lambda x: arr[x] == target, range(5)))
print(a)

