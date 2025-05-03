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
                            print("Alright! Let's get the show on the board!")
                            okay = True
                        else:
                            print("Error: Incorrect value! Please choose two values between 6 and 10.")
                    else:
                        print("Error: Incorrect value! Please choose two values between 6 and 10.")
                except ValueError:
                    print("Error: No integer detected! Please try again.")
            if okay == True:
                break
        else:
            print("Error: Unexpected text received! Please try again")
    return m, n

