import random

def get_ship_placements_p1(matrix):
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    while i < 4:
        lin = random.randint(0, m - 1)
        col = random.randint(0, n - 1)
        choice = random.randint(0, 1)
        print(lin, col, choice)
        okay = False
        # choice = H / V, Horizontal = False, Vertical = True
        if matrix[lin][col] == '-':
            # Destroyer Ship
            if i == 0:
                if choice == 0:
                    if col > 0 and matrix[lin][col - 1] == '-' :
                        matrix[lin][col] = matrix[lin][col - 1] = 'D'
                        okay = True
                    elif col < n - 1 and matrix[lin][col + 1] == '-':
                        matrix[lin][col] = matrix[lin][col + 1] = 'D'
                        okay = True
                elif choice == 1:
                    if lin > 0 and matrix[lin - 1][col] == '-':
                        matrix[lin][col] = matrix[lin - 1][col] = 'D'
                        okay = True
                    elif lin < m - 1 and matrix[lin + 1][col] == '-':
                        matrix[lin][col] = matrix[lin + 1][col] = 'D'
                        okay = True
            # Submarine Ship
            elif i == 1:
                if choice == 0:
                    if col > 1 and matrix[lin][col - 1] == '-' and matrix[lin][col - 2] == '-':
                        matrix[lin][col] = matrix[lin][col - 1] = matrix[lin][col - 2] = 'S'
                        okay = True
                    elif col < n - 2 and matrix[lin][col + 1] == '-' and matrix[lin][col + 2] == '-':
                        matrix[lin][col] = matrix[lin][col + 1] = matrix[lin][col + 2] = 'S'
                        okay = True
                elif choice == 1:
                    if lin > 1 and matrix[lin - 1][col] == '-' and matrix[lin - 2][col] == '-':
                        matrix[lin][col] = matrix[lin - 1][col] = matrix[lin - 2][col] = 'S'
                        okay = True
                    elif lin < m - 2 and matrix[lin + 1][col] == '-' and matrix[lin + 2][col] == '-':
                        matrix[lin][col] = matrix[lin + 1][col] = matrix[lin + 2][col] = 'S'
                        okay = True
            # Cruiser Ship
            elif i == 2:
                if choice == 0:
                    if col > 2 and matrix[lin][col - 1] == '-' and matrix[lin][col - 2] == '-' and matrix[lin][col - 3] == '-':
                        matrix[lin][col] = matrix[lin][col - 1] = matrix[lin][col - 2] = matrix[lin][col - 3] = 'C'
                        okay = True
                    elif col < n - 3 and matrix[lin][col + 1] == '-' and matrix[lin][col + 2] == '-' and matrix[lin][col + 3] == '-':
                        matrix[lin][col] = matrix[lin][col + 1] = matrix[lin][col + 2] = matrix[lin][col + 3] = 'C'
                        okay = True
                elif choice == 1:
                    if lin > 2 and matrix[lin - 1][col] == '-' and matrix[lin - 2][col] == '-' and matrix[lin - 3][col] == '-':
                        matrix[lin][col] = matrix[lin - 1][col] = matrix[lin - 2][col] = matrix[lin - 3][col] = 'C'
                        okay = True
                    elif lin < m - 3 and matrix[lin + 1][col] == '-' and matrix[lin + 2][col] == '-' and matrix[lin + 3][col] == '-':
                        matrix[lin][col] = matrix[lin + 1][col] = matrix[lin + 2][col] = matrix[lin + 3][col] = 'C'
                        okay = True
            # Battleship
            elif i == 3:
                if choice == 0:
                    if col > 3 and matrix[lin][col - 1] == '-' and matrix[lin][col - 2] == '-' and matrix[lin][col - 3] == '-' and matrix[lin][col - 4] == '-':
                        matrix[lin][col] = matrix[lin][col - 1] = matrix[lin][col - 2] = matrix[lin][col - 3] = matrix[lin][col - 4] = 'B'
                        okay = True
                    elif col < n - 4 and matrix[lin][col + 1] == '-' and matrix[lin][col + 2] == '-' and matrix[lin][col + 3] == '-' and matrix[lin][col + 4] == '-':
                        matrix[lin][col] = matrix[lin][col + 1] = matrix[lin][col + 2] = matrix[lin][col + 3] = matrix[lin][col + 4] = 'B'
                        okay = True
                elif choice == 1:
                    if lin > 3 and matrix[lin - 1][col] == '-' and matrix[lin - 2][col] == '-' and matrix[lin - 3][col] == '-' and matrix[lin - 4][col] == '-':
                        matrix[lin][col] = matrix[lin - 1][col] = matrix[lin - 2][col] = matrix[lin - 3][col] = matrix[lin - 4][col] = 'B'
                        okay = True
                    elif lin < m - 4 and matrix[lin + 1][col] == '-' and matrix[lin + 2][col] == '-' and matrix[lin + 3][col] == '-' and matrix[lin + 4][col] == '-':
                        matrix[lin][col] = matrix[lin + 1][col] = matrix[lin + 2][col] = matrix[lin + 3][col] = matrix[lin + 4][col] = 'B'
                        okay = True
        if okay == True:
            i += 1
    return matrix