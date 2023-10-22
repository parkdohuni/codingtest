def solution(board):
    answer = 0
    x = 0
    y = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                x = i
                y = j
                break

    print(x)
    print(y)
    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# print(solution([".D.R", "....", ".G..", "...D"]	))
