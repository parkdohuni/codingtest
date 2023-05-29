from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([i, p] for i, p in enumerate(priorities))
    while q:
        cur = q.popleft()
        if any(cur[1] < p[1] for p in q):
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break
    print(answer)
    return answer


solution([3, 1, 4, 2], 0)
solution([3, 1, 4, 2], 1)
solution([3, 1, 4, 2], 2)
solution([3, 1, 4, 2], 3)
solution([2, 1, 3, 2], 0)
solution([2, 1, 3, 2], 1)
solution([2, 1, 3, 2], 2)
solution([2, 1, 3, 2], 3)
solution([1, 1, 9, 1, 1, 1], 0)
solution([1, 1, 9, 1, 1, 1], 1)
solution([1, 1, 9, 1, 1, 1], 2)
solution([1, 1, 9, 1, 1, 1], 3)
solution([1, 1, 9, 1, 1, 1], 4)
solution([1, 1, 9, 1, 1, 1], 5)
