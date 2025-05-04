def check_end(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    active_ships={
        'D': 0,
        'S': 0,
        'C': 0,
        'B': 0
    }
    
    for i in range(rows):
        for j in range(cols):
            ship=matrix[i][j]
            if ship in 'DSCB':
                return 0
    return 1
