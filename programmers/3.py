def solution(sequence, k):
    answer = []
    sum = 0
    s = 0
    e = -1
    while 1:
        if sum < k:
            e += 1
            if e >= len(sequence):
                break
            sum += sequence[e]
        else:
            sum -= sequence[s]
            if s >= len(sequence):
                break
            s += 1

        if sum == k:
            answer.append([s, e])

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))
