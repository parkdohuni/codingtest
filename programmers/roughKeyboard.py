def solution(keymap, targets):
    answer = []
    alp_key = dict()  # 각 문자에 대한 키 정보를 저장할 딕셔너리

    for key in keymap:
        for idx, alp in enumerate(key):

            if (alp in alp_key) and (idx + 1) > alp_key[alp]:
                continue

            alp_key[alp] = idx + 1
    for target in targets:
        total = 0
        for alp in target:
            if alp in alp_key:
                total += alp_key[alp]
            else:
                total = - 1
                break
        answer.append(total)
    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"]))
print(solution(["AA"], ["B"]))
