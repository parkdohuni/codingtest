def solution(park, routes):
    answer = []
    x_len = len(park)
    y_len = len(park[0])

    for i in range(x_len):
        for j in range(y_len):
            if park[i][j] == "S":
                answer.append([i, j])
                start_y = j
                start_x = i
                move_y = j
                move_x = i
    for move in routes:
        if move[0] == "E":
            move_y += int(move[2])
            for i in range(1, int(move[2]) + 1):
                if start_y + i < y_len and park[start_x][start_y + i] == "X":
                    move_y -= int(move[2])
                    break
            if move_y >= y_len:
                move_y -= int(move[2])
            else:
                answer.append([move_x, move_y])
                start_y = move_y
        elif move[0] == "W":
            move_y -= int(move[2])
            for i in range(1, int(move[2]) + 1):
                if start_y - i < y_len and move_y >= 0 and park[start_x][start_y - i] == "X":
                    move_y += int(move[2])
                    break
            if move_y >= y_len or move_y < 0:
                move_y += int(move[2])
            else:
                answer.append([move_x, move_y])

                start_y = move_y
        elif move[0] == "N":
            move_x -= int(move[2])
            for i in range(1, int(move[2]) + 1):
                if start_x - i < x_len and move_x >= 0 and park[start_x - i][start_y] == "X":
                    move_x += int(move[2])
                    break
            if move_x >= x_len or move_x < 0:
                move_x += int(move[2])
            else:
                answer.append([move_x, move_y])

                start_x = move_x
        elif move[0] == "S":
            move_x += int(move[2])
            for i in range(1, int(move[2]) + 1):
                if start_x + i < x_len and park[start_x + i][start_y] == "X":
                    move_x -= int(move[2])
                    break
            if move_x >= x_len:
                move_x -= int(move[2])
            else:
                answer.append([move_x, move_y])

                start_x = move_x
    return answer.pop()


# print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
# print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))
# print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
# print(solution(["SOO", "OOO", "OOO"], ["W 2", "S 2", "E 1"]))
print(solution(["SXX", "XXX", "XXO"], ["W 3", "N 1"]))
print(solution(["XXX", "XXX", "XXS"], ["E 2", "S 1"]))
