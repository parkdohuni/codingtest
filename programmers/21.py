def solution(k, tangerine):
    answer = 0
    a = {}
    for i in tangerine:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    a = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
    for i in a:
        if k <= 0:
            return answer
        k -= a[i]
        answer += 1
    return answer


solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
solution(4, [1, 3, 2, 5, 4, 5, 2, 3])
solution(2, [1, 1, 1, 1, 2, 2, 2, 3])
