ship_dict = {
    0: ("Destroyer", 2),
    1: ("Submarine", 3),
    2: ("Cruiser", 4),
    3: ("Battleship", 5),
}
letters_to_num = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
}

s = "ABCDEFGHI"


def create_empty_board(m, n):
    return [["-" for _ in range(n)] for _ in range(m)]


def free_area(lnstart, lnstop, colstart, colstop, matrix):
    free = True
    for row in range(lnstart, lnstop + 1):
        for col in range(colstart, colstop + 1):
            if matrix[row][col] != "-":
                free = False
                break
        if not free:
            break
    return free


def vertical_position(matrix, ship_size, ship_name):
    print(f"Place your {ship_name} (e.g.: A0A1).")
    while True:
        position = input().strip().upper()

        if len(position) != 4:
            print("Error. Enter a valid position (e.g. A0A1)")
            continue
        try:
            lnstart = int(position[1])
            lnstop = int(position[3])
            colstart = letters_to_num[(position[0])]
            colstop = letters_to_num[(position[2])]
        except (ValueError, KeyError):
            print("Invalid input. Please follow the format A0A1.")
            continue

        if colstart != colstop:
            print("Error. Place your ship vertically.")
        elif abs(lnstart - lnstop) != ship_size - 1:
            print(f"Error. Please select an area of {ship_size} cells.")
        elif free_area(lnstart, lnstop, colstart, colstop, matrix):
            return lnstart, lnstop, colstart, 3
        else:
            print("Error. You have already placed a ship there.")
            print(f"Choose: 1 to replace {ship_name} or 2 to replace all ships")
            option = input().strip()
            while option not in "12":
                print("Choose a valid option (1/2).")
                option = input().strip()
            option = int(option)
            if option == 1:
                return 0, 0, 0, 1
            elif option == 2:
                return 0, 0, 0, 2


def horizontal_position(matrix, ship_size, ship_name):
    print(f"Place your {ship_name} (e.g.: A0A1).")
    while True:
        position = input().strip().upper()

        if len(position) != 4:
            print("Error. Enter a valid position (e.g. A0B0b)")
            continue
        try:
            lnstart = int(position[1])
            lnstop = int(position[3])
            colstart = letters_to_num[(position[0])]
            colstop = letters_to_num[(position[2])]
        except (ValueError, KeyError):
            print("Invalid input. Please follow the format A0A1.")
            continue

        if lnstart != lnstop:
            print("Error. Place your ship horizontally.")
        elif abs(colstart - colstop) != ship_size - 1:
            print(f"Error. Please select an area of {ship_size} cells.")
        elif free_area(lnstart, lnstop, colstart, colstop, matrix):
            return lnstart, colstart, colstop, 3
        else:
            print("Error. You have already placed a ship there.")
            print(f"Choose: 1 to replace {ship_name} or 2 to replace all ships")
            option = input().strip()
            while option not in "12":
                print("Choose a valid option (1/2).")
                option = input().strip()
            option = int(option)
            if option == 1:
                return 0, 0, 0, 1
            elif option == 2:
                return 0, 0, 0, 2


def place_ships(matrix):
    m = len(matrix)
    n = len(matrix[0])
    final_matrix = create_empty_board(m, n)
    ship = 0
    while ship < 4:
        ship_name, ship_size = ship_dict[ship]
        print(f"Please, place your {ship_name}.\n")
        print("Position options:\n")
        print("1 - vertical\n")
        print("2 - horizontal\n")
        choice = input().strip()
        while choice not in "12":
            print("Choose a valid option (1/2).")
            choice = input().strip()
            # placed=False
            # while not placed:
        if choice == "1":
            lnstart, lnstop, col, next_action = vertical_position(
                final_matrix, ship_size, ship_name
            )
            if next_action == 3:  # valid vertical position
                for row in range(lnstart, lnstop + 1):
                    final_matrix[row][col] = ship_name[0]
            elif next_action == 2:  # replace all ships
                final_matrix = create_empty_board(m, n)  # reset board
                ship = -1
            elif next_action == 1:  # replace current ship
                ship -= 1
            ship += 1
        else:
            ln, colstart, colstop, next_action = horizontal_position(
                final_matrix, ship_size, ship_name
            )
            if next_action == 3:
                for col in range(colstart, colstop + 1):
                    final_matrix[ln][col] = ship_name[0]
            elif next_action == 2:
                final_matrix = create_empty_board(m, n)
                ship = -1
            elif next_action == 1:
                ship -= 1
            ship += 1
    return final_matrix
