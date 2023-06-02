def solution(s):
    answer = []
    arr = list(map(int, s.split()))
    a = min(arr)
    b = max(arr)
    answer.append(a)
    answer.append(b)

    return " ".join(map(str, answer))

print(solution("1 2 3 4"))
