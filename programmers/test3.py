def solution(events, limit):
    answer = []
    time = events[-1]
    before = 0
    after = time

    while 1:
        cnt = 0
        flag = 1
        for event in events:
            if before <= event < after:
                cnt += 1
                flag = 1
                answer.append(event)
            if cnt > limit:
                answer.clear()
                flag = 0
                break
            if len(events) == len(answer):
                return time
        if flag:
            before += time
            after += time
        else:
            time -= 1
            before = 0
            after = time

    return time

# 테스트 케이스
print(solution([3, 7, 8], 1))  # 출력: 4
print(solution([3, 7, 8], 2))  # 출력: 8
print(solution([0, 1, 2, 3, 4, 5, 6], 2))  # 출력: 1
print(solution([1, 2, 3, 4, 5, 6], 2))  # 출력: 2
print(solution([1, 2, 3, 4, 5, 6], 3))  # 출력: 2
print(solution([1, 2, 3, 4, 5, 6], 4))  # 출력: 2
print(solution([1, 2, 3, 4, 5, 6], 5))  # 출력: 2
print(solution([1, 2, 3, 4, 5, 6], 6))  # 출력: 2


