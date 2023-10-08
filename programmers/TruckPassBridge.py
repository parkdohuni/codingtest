from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(10000)]
    queue = deque(truck_weights)
    isbridge = deque(bridge, maxlen=bridge_length)
    bgsum = sum(isbridge)
    while True:
        if len(queue) == 0:
            return answer + bridge_length
        if bgsum - isbridge[0] + queue[0] <= weight:
            bgsum -= isbridge[0]
            bgsum += queue[0]
            isbridge.append(queue.popleft())
        else:
            bgsum -= isbridge[0]
            isbridge.append(0)
        answer += 1
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
