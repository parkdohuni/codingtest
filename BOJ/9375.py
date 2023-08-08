import sys

read = sys.stdin.readline

tc = int(read())
for _ in range(tc):
    n = int(read())
    dic = {}
    ans = 1
    num = 1
    for _ in range(n):
        name, cloth = map(str, read().rstrip().split())
        if cloth in dic.keys():
            num = dic[cloth] + 1
        else:
            num = 1
        dic[cloth] = num
    for i in dic:
        ans *= (dic[i] + 1)
    print(ans - 1)
