import re
from check_end import check_end
from check_sink import check_sink
from print_grid import print_grid

def player_go(matrix, hidden_matrix):
    m = len(matrix)
    n = len(matrix[0])
    okay = False
    while okay == False:
        print("Choose your target! (e.g.: A0)")
        target = input().strip().upper()
        if len(target) != 2:
            print("Error: Invalid target")
        else:
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
                        matrix[lin][col] = 'H'
                        prev_char = hidden_matrix[lin][col]
                        hidden_matrix[lin][col] = 'H'
                        if check_end(matrix) == True:
                            print_grid(matrix)
                            print("Game over. Player 1 sunk all the ships!")
                            okay = True
                        elif check_sink(hidden_matrix, prev_char) == True:
                            print("You sunk the", end = " ")
                            if prev_char == 'D':
                                print("Destroyer")
                            elif prev_char == 'S':
                                print("Submarine")
                            elif prev_char == 'C':
                                print("Cruiser")
                            elif prev_char == 'B':
                                print("Battleship")
                        else:
                            print("HIT!")
                    else:
                        print("MISS!")
                        matrix[lin][col] = 'M'
                else:
                    print("Error: You've already hit this target before!")
                print_grid(matrix)
            else:
                print("Error: Invalid target!")
    return matrix
