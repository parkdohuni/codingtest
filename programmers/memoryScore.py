def solution(name, yearning, photo):
    answer = []
    name_dic = dict(zip(name, yearning))
    for people in photo:
        score = 0
        for name in people:
            score += name_dic.get(name, 0)
        answer.append(score)
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
