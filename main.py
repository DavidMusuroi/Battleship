from init_grids import get_grids_length as length
from init_grids import get_matrix as mat
from beginning import beginning_game as start
from place_ships_p1 import get_ship_placements_p1 as ships_p1
from place_ships_p2 import place_ships as ships_p2
from player_turn import player_go
from check_end import check_end
from print_grid import print_grid

start()
m, n = length()
p1_matrix = mat(m, n)
p2_matrix = mat(m, n)
end = False

p1_hidden_matrix = ships_p1(p1_matrix)
p1_matrix = mat(m, n)
p2_hidden_matrix = ships_p2(p2_matrix)

print("\n----Player 1 - Hidden ---\n")
print_grid(p1_hidden_matrix)
print("----Player 2 - Hidden ---\n")
print_grid(p2_hidden_matrix)

while end == False:
    p2_matrix = player_go(p2_matrix, p2_hidden_matrix)
    if check_end(p2_matrix) == True:
        print("Here was the original setup of player 1's ships:")
        print_grid(p1_hidden_matrix)
        print("You got this far:")
        print_grid(p1_matrix)
        break
    else:
        print("The game continues. It's player 2's turn.")
    p1_matrix = player_go(p1_matrix, p1_hidden_matrix)
    if check_end(p1_matrix) == True:
        print("Here was the original setup of player 2's ships:")
        print_grid(p2_hidden_matrix)
        print("You got this far:")
        print_grid(p2_matrix)
        break
    else:
        print("The game continues. It's player 1's turn.")
