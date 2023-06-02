#다시
def solution(picks, minerals):
    answer = 0

    sum = 0
    for pick in picks:
        sum += pick

    num_minerals = sum * 5
    if num_minerals < len(minerals):
        minerals = minerals[:num_minerals]

    cnt_min = [[0, 0, 0] for _ in range(10)]

    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            cnt_min[i // 5][0] += 1
        elif minerals[i] == "iron":
            cnt_min[i // 5][1] += 1
        else:
            cnt_min[i // 5][2] += 1

    sort_cnt_minerals = sorted(cnt_min, key=lambda x: (-x[0], -x[1], -x[2]))

    for idx in sort_cnt_minerals:
        d, i, s = idx
        for k in range(len(picks)):
            if k == 0 and picks[k] > 0:
                picks[k] -= 1
                answer += d + i + s
                break
            elif k == 1 and picks[k] > 0:
                picks[k] -= 1
                answer += d * 5 + i + s
                break
            elif k == 2 and picks[k] > 0:
                picks[k] -= 1
                answer += d * 25 + i * 5 + s
                break

    return answer


solution([1, 0, 1], ["iron", "iron", "iron", "iron", "diamond", "diamond", "diamond"])
solution([1, 1, 1],
         ["diamond", "stone", "stone", "diamond", "stone", "iron", "iron", "iron", "iron", "iron", "diamond"])
