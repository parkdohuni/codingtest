def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    idx = 0
    for i in citations:
        idx += 1
        if idx <= i:
            answer += 1
    print(answer)
    return answer


solution([3, 0, 6, 1, 5, 7])
