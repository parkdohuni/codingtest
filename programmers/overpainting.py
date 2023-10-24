def solution(n, m, section):
    paint, answer = section[0] - 1, 0
    for s in section:
        if paint < s:
            paint = s + m - 1
            answer += 1

    return answer


print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 2, [4]))
