def solution(k, a, b, init_password, times):
    answer = []
    otp = []
    password = int(init_password)
    otp.append(password)

    for _ in range(10000):
        new_password = (a * password + b) % 10000
        otp.append(new_password)
        password = new_password
    print(otp)

    for time in times:
        idx = time // k
        answer.append(format(otp[idx], '04d'))
    return answer


# print(solution(30, 25, 13, "0001", [0, 29, 30, 119, 120, 10000]))
print(solution(1, 1, 1, "0001", [2, 3, 4, 10000]))
# print(solution(100, 1, 1000, "7123", [100, 10000, 1]))
