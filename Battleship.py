import random
from Ship import Ship
from Coord import Coord
print("Battleship!!!")

players = input("Select between 1 or 2 players: ")
if players != "2"  and players != "2" :
    while players != "1" and players != "2":
        players = input("Select between 1 or 2 players: ")

print("1) Easy Mode")
print("2) Normal Mode")
print("3) Hard Mode")

mode = input("Select a diffculty mode from the following above: ")
if mode != "1" and mode != "2" and mode != "3":
    while mode != "1" and mode != "2" and mode != "3":
        mode = mode = input("Select a diffculty mode from the following above: ")

board = []
length = 0
if players == "1":
    if mode == "1":
        board = [["~"] * 5 for _ in range(5)]
        boardships = [["~"] * 5 for _ in range(5)]
        length = 5
    if mode == "2":
            board = [["~"] * 8 for _ in range(8)]
            boardships = [["~"] * 8 for _ in range(8)]
            length = 8 
    if mode == "3":
            board = [["~"] * 10 for _ in range(10)]
            boardships = [["~"] * 10 for _ in range(10)]
            length = 10

    for row in board:
        print(" ".join(row))

    Targets = 0

    Ship1 = Ship(2, length, boardships)
    boardships = Ship1.setBoard(boardships)
    Targets += 2
    Ship2 = Ship(3, length, boardships)
    boardships = Ship2.setBoard(boardships)
    Targets += 3
    if mode == "2":
        Ship3 = Ship(3,length,boardships)
        boardships = Ship3.setBoard(boardships)
        Targets += 3
        Ship4 = Ship(3,length,boardships)
        boardships = Ship4.setBoard(boardships)
        Targets += 3
    if mode == "3":
        Ship5 = Ship(4,length,boardships)
        boardships = Ship5.setBoard(boardships)
        Targets += 4
        Ship6 = Ship(5,length,boardships)
        boardships = Ship6.setBoard(boardships)
        Targets += 5
        Ship7 = Ship(5,length,boardships)
        boardships = Ship7.setBoard(boardships)
        Targets += 5

    
    if mode == "1":
        Shots = 15
    if mode == "2":
        Shots = 38
    if mode == "3":
        Shots = 50

    Hits = 0
    for row in board:
        print(" ".join(row))
    while Shots != 0 and Hits != Targets:

        print(f"{Shots} shots left")
        x = int(input("Enter the X coordinate on the board:"))
        y = int(input("Now, Enter the Y coordinate on the board:"))
        if x >= length or y >= length or board[x][y] != "~":
            Newcoord = False
            while Newcoord == False:
                x = int(input("Enter the X coordinate on the board:"))
                y = int(input("Now, Enter the Y coordinate on the board:"))
                if (x < length or y < length) and board[x][y] == "~":
                    Newcoord = True

        if boardships[x][y] == "S":
            board[x][y] = "X"
            Hits += 1
            Shots -= 1
            for row in board:
                print(" ".join(row))
            print("A ship has been hit!!!")
        else:
            board[x][y] = "O"
            Shots -= 1
            for row in board:
                print(" ".join(row))
            print("Missed...")


    if Hits == Targets:
        print("YOU WIN!!!")
    else:
        print("you lose...")
                    


        
    
    
    



                    
                               


    