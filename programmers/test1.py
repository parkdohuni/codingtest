def solution(matrix, r):
    n = len(matrix)

    for _ in range(r):
        new_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new_matrix[j][n - i - 1] = matrix[i][j]

        matrix = new_matrix
    return matrix

# print(solution([[1, 2], [3, 4]], 1))
# print(solution([[1, 2], [3, 4]], 2))
# print(solution([[4, 1, 2], [7, 3, 4], [3, 5, 6]], 3))
