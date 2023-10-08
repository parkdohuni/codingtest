def solution(clothes):
    dict = {}
    for cloth, type in clothes:
        dict[type] = dict.get(type, 0) + 1

    answer = 1
    for type in dict:
        answer *= (dict[type] + 1)
    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
