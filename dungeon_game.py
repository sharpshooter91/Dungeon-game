import random
import os
#draw the grid
#pick random location for the player
#pick random location for exit door
#random location for the monster
#draw player in the grid
#take input for movement
#move the player, unless invalid move (past edges of the grid)
#check for win/lose
#clear screen and redraw grid

CEELS = [(0, 0), (1, 0), (2, 0), (3, 0),(4, 0),
                (0, 1), (1, 1), (2, 1), (3, 1),(4, 1),
                (0, 2), (1, 2), (2, 2), (3, 2),(4, 2),
                (0, 3), (1, 3), (2, 3), (3, 3),(4, 3),
                (0, 4), (1, 4), (2, 4), (3, 4),(4, 4)]

def clear_scr():
    os.system('cls' if os.name== "nt" else "clear")

def get_location():
    return random.sample(CEELS, 3)


def move_player(player, move):
    x, y= player
    if move.upper()== "LEFT":
        x= x-1
    if move.upper()== "RIGHT":
        x= x+1
    if move.upper()== "UP":
        y= y-1
    if move.upper()== "DOWN":
        y= y+1
    return x, y

def get_moves(player):
    moves= ['LEFT', 'RIGHT', 'UP', "DOWN"]
    x, y= player
    if x == 0:
        moves.remove("LEFT")
    if x== 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves

def draw_map(player):
    print(" _"*5)
    tile= "|{}"
    for cell in CEELS:
        x,y= cell
        if x< 4:
            line_end= ""
            if cell== player:
                output= tile.format("X")
            else:
                output= tile.format("_")
        else:
            line_end= "\n"
            if cell== player:
                output= tile.format("X|")
            else:
                output= tile.format("_|")
        print(output, end= line_end)



def game_loop():
    monster, door, player= get_location()
    playing= True

    while playing:
        clear_scr()
        draw_map(player)
        valid_moves= get_moves(player)

        print("you are currently in a room {}".format(player)) #fil it with players position
        print("You can move {}".format(", ".join(valid_moves))) #fill with available moves
        print("Enter QUIT to quit")

        move = input(">  ")
        move= move.upper()

        if move == "QUIT":
            print("\n ** See you next time! **\n")
            break

        if move in valid_moves:
            player= move_player(player, move)
            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time!** \n")
                playing= False
            if player == door:
                print("\n ** You escape! CONGRATULATION!!!")
                playing= False
        else:
            input("\n **Walls are hard don't run into them! **\n")
    else:
        if  input("Play again?  [Y/n]  ").lower() != "n":
            game_loop()


clear_scr()
print("Welcome to the dungeon!")
input("press return to start")
clear_scr()
game_loop()

    #Good move > change the player position
    #Bad move? Do not change anythng
    # On the door? They win:
    #On the monster? They loos!
    #Othervise? Loop back around
