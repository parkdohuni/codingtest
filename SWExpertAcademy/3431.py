t = int(input())

for i in range(t):
    l, u, x = map(int, input().split())
    if x < l:
        print("#{} {}".format(i + 1, l - x))
    elif l < x < u:
        print("#{} {}".format(i + 1, 0))
    elif u < x:
        print("#{} {}".format(i + 1, -1))
