from init_grids import get_grids_length as length
from init_grids import get_matrix as mat
from beginning import beginning_game as start
from place_ships_p1 import get_ship_placements_p1 as ships_p1
from place_ships_p2 import place_ships as ships_p2
from player_turn import player_go as go
from check_end import check_end
from print_grid import print_grid

start()
m, n = length()
p1_matrix = mat(m, n)
p2_matrix = mat(m, n)
dict_ships = {"Destroyer": 2, "Submarine": 3, "Cruiser": 4, "Battleship": 5}

p1_hidden_matrix = ships_p1(p1_matrix)

print("----Player 1 - Hidden ---\n")
print_grid(p1_hidden_matrix)

# for i in range(m):
#     for j in range(n):
#         print(p1_hidden_matrix[i][j], end = " ")
#     print("\n")

# go(p1_hidden_matrix)

p2_hidden_matrix = ships_p2(p2_matrix)
print("----Player 2 - Hidden ---\n")
print_grid(p2_hidden_matrix)


if check_end(p1_matrix) == 1:
    print("Game over. Player 1 won!")
else:
    print("The game continues. It's player 2's turn.")
