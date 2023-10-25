from collections import Counter


def solution(topping):
    answer = 0
    a = Counter(topping)
    b = set()
    for i in topping:
        a[i] -= 1
        if a[i] == 0:
            del a[i]
        b.add(i)
        if len(a) == len(b):
            answer += 1
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))
