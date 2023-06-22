def solution(n, words):
    answer = [0, 1]
    save = words[0][0]
    stack = []
    for i in words:
        answer[0] += 1
        if answer[0] > n:
            answer[1] += 1
            answer[0] = 1

        if save != i[0]:
            return answer
        save = i[-1]

        if stack.__contains__(i):
            return answer
        stack.append(i)

    answer = [0, 0]
    return answer


solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
#11 21 31 12 22 32 13 23 33
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
             "gather", "refer", "reference", "estimate", "executive"])
solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
