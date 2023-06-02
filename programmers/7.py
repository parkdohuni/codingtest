from collections import deque


def solution(progresses, speeds):
    answer = []
    arr = deque()
    speed = deque()
    date = deque()
    for i in range(len(progresses)):
        arr.append(progresses[i])
        speed.append(speeds[i])
    idx = 0
    while arr:
        a = arr.popleft()
        b = speed.popleft()
        x = 100 - a
        if x % b != 0:
            y = (x // b) + 1
        else:
            y = x // b
        date.append(y)
    ans = 1
    for j in range(1, len(date)):
        if date[idx] < date[j]:
            idx = j
            answer.append(ans)
            ans = 1
        else:
            ans += 1
    answer.append(ans)
    print(answer)
    return answer


solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
