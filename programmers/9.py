#BFS 풀이
def solution(numbers, target):
    answer = 0
    leave = [0]
    for num in numbers:
        temp = []
        for i in leave:
            temp.append(i + num)
            temp.append(i - num)
        leave = temp
    for k in leave:
        if k == target:
            answer += 1
    return answer

solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)
