import sys

input = sys.stdin.readline
k, l = map(int, input().split())
dic = {}
for i in range(l):
    num = input().rstrip()
    dic[num] = i
sort_dic = sorted(dic.items(), key=lambda x: x[1])
if k > len(sort_dic):
    k = len(sort_dic)

for i in range(k):
    print(sort_dic[i][0])
