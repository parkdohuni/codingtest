def solution(numbers):
    answer = []
    big = 0
    save = 0
    for number in reversed(numbers):
        if number > big:
            big = number
            answer.append(-1)
        elif number < save:
            answer.append(save)
            big = save
            save = number
        elif number <= big:
            answer.append(big)
            save = number

    return list(reversed(answer))


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
print(solution([1,2,1,2,1,2,1,9]))
