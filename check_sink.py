def check_sink(matrix, char):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == char:
                return False
    return True