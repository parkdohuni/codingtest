def solution(brown, yellow):
    answer = []
    arr = []
    num = brown + yellow
    for i in range(1, num + 1):
        if num % i == 0:
            arr.append(i)
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        a = mid - 1
        b = mid
    else:
        a = mid
        b = mid

    while 1:
        if (arr[a] - 2) * (arr[b] - 2) == yellow:
            return [arr[b], arr[a]]
        else:
            a -= 1
            b += 1

    return answer


print(solution(10, 2))

print(solution(8, 1))
print(solution(24, 24))
print(solution(14, 4))
