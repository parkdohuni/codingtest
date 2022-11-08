#1620번 나는야 포켓몬 마스터 이다솜
import sys

input = sys.stdin.readline
n ,m = map(int, input().split())

int_key_dic = {}
name_key_dic = {}

for i in range(n):
    name = input().rstrip()
    int_key_dic[i] = name
    name_key_dic[name] = i

for _ in range(m):
    k = input().rstrip()
    if k.isdigit() == True:
        print(int_key_dic[int(k) - 1])
    else:
        print(name_key_dic[k] + 1)