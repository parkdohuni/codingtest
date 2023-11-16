tc = int(input())
for t in range(1, tc + 1):
    a, b = map(int, input().split())
    if b == 1:
        print("#{} {}".format(t, a * a))
    elif a == b:
        print("#{} {}".format(t, 1))
    elif a % b == 0:
        a = a // b
        print("#{} {}".format(t, a * a))
