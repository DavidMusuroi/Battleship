def check_end(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    total_hits = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != '-':
                total_hits += 1
    if total_hits == 14:
        return True
    else:
        return False
