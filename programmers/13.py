from collections import deque


def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    while q:
        if len(q) == 1:
            q.pop()
            answer += 1
            break
        sum = q[0] + q[-1]
        if sum > limit:
            q.pop()
            answer += 1
        else:
            q.pop()
            q.popleft()
            answer += 1
    print(answer)

    return answer


solution([70, 50, 80, 50], 100)
solution([70, 50, 80], 100)
