# 폰켓몬

def solution(nums):
    answer = 0
    dic = dict()
    for i in range(len(nums)):
        if len(dic) == len(nums) // 2:
            return answer
        if nums[i] in dic.values():
            continue
        else:
            dic[answer] = nums[i]
            answer += 1
    return answer


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
