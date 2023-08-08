import sys
read = sys.stdin.readline
n, m = map(int, read().split())
dic = {}
for _ in range(n):
    group = str(read().rstrip())
    num = int(read())
    name = []
    for _ in range(num):
        temp = str(read().rstrip())
        name.append(temp)
        dic[temp] = group
    name = sorted(name)
    dic[group] = name


for _ in range(m):
    quiz = str(read().rstrip())
    case = int(read())
    if case == 1:
        print(dic[quiz])
    else:
        print("\n".join(dic[quiz]))