def solution(s):
    answer = []
    a = s.split(" ")
    for i in a:
        if i:
            answer.append(i[0].upper() + i[1:].lower())
        else:
            answer.append(i)

    return " ".join(answer)