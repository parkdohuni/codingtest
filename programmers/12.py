def solution(name):
    answer = 0
    name_len = len(name)
    move_count = name_len - 1  # 왼쪽 또는 오른쪽으로 이동하는 횟수

    for i in range(name_len):
        # 알파벳 조작 횟수 계산
        diff = ord(name[i]) - ord('A')
        answer += min(diff, 26 - diff)

        # 커서 이동 최소 횟수 계산
        next_idx = i + 1
        while next_idx < name_len and name[next_idx] == 'A':
            next_idx += 1
        # 현재 위치에서 왼쪽으로 이동하여 다음 위치로 가는 경우와 오른쪽으로 이동하여 다음 위치로 가는 경우 중 최소 이동 횟수 계산
        move_count = min(move_count, i + name_len - next_idx + min(i, name_len - next_idx))

    answer += move_count

    return answer

# solution("AABA")
solution("BABCC")
# solution("BCAAABCD")