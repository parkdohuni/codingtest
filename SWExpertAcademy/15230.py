
t = int(input())

for test_case in range(1, t + 1):
    alpha = list(input())
    ans = 0
    for i in range(len(alpha)):
        if ord(alpha[i]) == (ord('a') + i):
            ans += 1
        else: 
            break
    print("#{} {}".format(test_case, ans))  