def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    print(plans)
    stack = []
    for subject, start, time in plans:
        h, m = map(int, start.split(':'))
        start = 60 * h + m
        time = int(time)

        if stack:
            prev_subject, prev_start, prev_time = stack.pop()
            extra = start - prev_start

            if extra < prev_time:
                stack.append((prev_subject, prev_start, prev_time - extra))
            else:
                answer.append(prev_subject)
                extra = extra - prev_time

                while stack and extra:
                    prev_subject, prev_start, prev_time = stack.pop()
                    if extra < prev_time:
                        stack.append((prev_subject, prev_start, prev_time - extra))
                        break
                    else:
                        answer.append(prev_subject)
                        extra = extra - prev_time

        stack.append((subject, start, time))

    answer.extend([s for s, _, _ in stack[::-1]])
    return answer


# solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])
solution(
    [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])
solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])
