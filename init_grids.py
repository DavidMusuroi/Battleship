def get_grids_length():
    print("Would you like a classic board or a custom board?")
    while 1:
        choice = input()
        if choice == "classic":
            m = 6
            n = 6
            break
        elif choice == "custom":
            okay = False
            while okay == False:
                print("Please choose two values between 6 and 10: ")
                try:
                    m = int(input())
                    if 6 <= m <= 10:
                        n = int(input())
                        if 6 <= n <= 10:
                            okay = True
                        else:
                            print("Error: Incorrect value! Please choose two values between 6 and 10.")
                    else:
                        print("Error: Incorrect value! Please choose two values between 6 and 10.")
                except ValueError:
                    print("Error: No number detected! Please try again.")
            if okay == True:
                break
        else:
            print("Error: Unexpected text received! Please try again")
    print("\nAlright! Let's get the show on the board!", end = "\n\n")
    return m, n

def get_matrix(m = 6, n = 6):
    matrix = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append('-')
        matrix.append(tmp)
    return matrix