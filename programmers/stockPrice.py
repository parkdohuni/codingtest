from collections import deque
def solution(prices):
    answer = []
    que = deque(prices)
    while(que):
        price = que.popleft()
        cnt = 0
        for q in que:
            cnt += 1
            if price > q:
                break
        answer.append(cnt)
    return answer


print(solution([1, 2, 3, 2, 3]))
