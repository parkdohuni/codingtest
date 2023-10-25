def solution(s, skip, index):
    alps = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(skip))

    alps_num = len(alps)
    answer = ''

    for char in s:
        answer += alps[(alps.index(char) + index) % alps_num]

    return answer


solution("aukks", "wbqd", 5)
