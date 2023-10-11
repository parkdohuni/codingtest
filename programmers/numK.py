def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        arr = sorted(array[i - 1:j])
        answer.append(arr[command[2] - 1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
