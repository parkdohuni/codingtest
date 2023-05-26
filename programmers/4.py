def solution(plans):
    answer = []
    stop = []
    plans.sort(key=lambda x: (x[1]))
    print(plans)
    time = []
    ehour = 0
    emin = 0
    for i in range(len(plans)):
        if len(s) == 0:
            s = plans[i][1].split(":")
        shour, smin = list(map(int, s))

        if ehour > shour:
            stop.append([list(plans[i][0]), ehour, emin])
        elif ehour == shour:
            if emin > smin:
                stop.append([list(plans[i][0]), ehour, emin])
        
        ehour = shour
        emin = smin
        emin += list(map(int, plans[i][2]))
        while emin >= 60:
            emin -= 60
            ehour += 1

    return answer


solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])
solution(
    [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])
solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])
