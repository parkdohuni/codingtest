n = int(input())
cnt = 0


def cal(a, b, n):
    if n == 1:
        print(a, b)
        return
    else:
        cal(a, 6 - a - b, n - 1)
        print(a, b)
        cal(6 - a - b, b, n - 1)


print(2 ** n - 1)
cal(1, 3, n)
