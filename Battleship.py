print("Battleship!!!")

players = input("Select between 1 or 2 players: ")
if players != "2"  and players != "2" :
    while players != "1" and players != "2":
        players = input("Select between 1 or 2 players: ")

print("1) Easy Mode")
print("2) Medium Mode")
print("3) Hard Mode")

mode = input("Select a diffculty mode from the following above: ")
if mode != "1" and mode != "2" and mode != "3":
    while mode != "1" and mode != "2" and mode != "3":
        mode = mode = input("Select a diffculty mode from the following above: ")

board = []
length = 0
if players == "1":
    if mode == "1":
        board = [["O"] * 5 for _ in range(5)]
        length = 5
    if mode == "2":
            board = [["O"] * 8 for _ in range(8)]
            length = 8 
    if mode == "3":
            board = [["O"] * 11 for _ in range(11)]
            length = 11

    for row in board:
        print(" ".join(row))
    

