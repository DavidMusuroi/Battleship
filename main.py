from init_grids import get_grids_length as length
from init_grids import get_matrix as mat
from beginning import beginning_game as start
from place_ships_p1 import get_ship_placements_p1 as ships_p1
from player_turn import player_go as go

start()
m, n = length()
p1_matrix = mat(m, n)
p2_matrix = mat(m, n)
dict_ships = {
    "Destroyer" : 2,
    "Submarine" : 3,
    "Cruiser" : 4,
    "Battleship" : 5
}
p1_hidden_matrix = ships_p1(p1_matrix)
for i in range(m):
    for j in range(n):
        print(p1_hidden_matrix[i][j], end = " ")
    print("\n")
# go(p1_hidden_matrix)
