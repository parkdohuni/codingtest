from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    q_cards1 = deque(cards1)
    q_cards2 = deque(cards2)
    for word in goal:
        if q_cards1 and q_cards1[0] == word:
            q_cards1.popleft()
        elif q_cards2 and q_cards2[0] == word:
            q_cards2.popleft()
        else:
            answer = 'No'
            return answer
    return answer


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
