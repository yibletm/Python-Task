import random
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

    ms = False
    while ms == False:
        s1len = 2
        ran = random.randint(0,1)
        if ran == 0:
             orient = 'H'
        else:
            orient = 'V'

        ranx = random.randint(0,length-1)
        rany = random.randint(0,length-1)
        
    
    
    

def shipMake(ship, boardships):
    {
        ms = False
        while ms == False:
           
            ran = random.randint(0,1)
            if ran == 0:
                orient = 'H'
            else:
                orient = 'V'
    
            ranx = random.randint(0,length-1)
            rany = random.randint(0,length-1)
    }