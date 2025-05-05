import re
def player_go(matrix, hidden_matrix):
    m = len(matrix)
    n = len(matrix[0])
    okay = False
    while okay == False:
        print("Choose your target! (e.g.: A0)")
        target = input()
        letter = target[0]
        check_letter = chr(ord('A') + n - 1)
        number = int(target[1])
        if len(letter) == 1 and 'A' <= letter <= check_letter and 0 <= number <= m - 1:
            lin = number
            col = int(ord(letter) - 65)
            if hidden_matrix[lin][col] != 'H':
                okay = True
                if hidden_matrix[lin][col] != '-':
                    okay = False
                    hidden_matrix[lin][col] = 'H'
                    matrix[lin][col] = 'H'
                    print("HIT!")
                    check_end(matrix)
                else:
                    print("MISS!")
                    matrix[lin][col] = 'M'
            else:
                print("Error: You've already hit this target before!")
        else:
            print("Error: Invalid target!")
    return matrix
