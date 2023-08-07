import sys

read = sys.stdin.readline
n = int(read())
dic = {}
for _ in range(n):
    name, log = map(str, read().rstrip().split())
    if log == "enter":
        dic[name] = True
    else:
        del dic[name]

dic = sorted(dic.keys(), reverse=True)
print("\n".join(dic))