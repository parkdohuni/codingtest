import sys

t = int(sys.stdin.readline())

for test_case in range(1, t + 1):
    n = int(sys.stdin.readline())
    if n % 2 == 0:
        print("#{} {}".format(test_case, "Alice"))
    else:
        print("#{} {}".format(test_case, "Bob"))
