import pygame
import random

pygame.init()

#Setting the screen size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# Displaying the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Allows us to display images using the word image
pygame.display.set_caption('image')

# Givng the player options to choose from
Player_Rock = False
Player_Paper = False
Player_Scissors = False

# Options that the Compute can choose
Computer_Rock = False
Compute_Paper = False
Computer_Scissors = False

# This is the Computers decisions
Computer_Decision = ""

# Shows if the player wins, loses, or ties
Win = False
Lose =  False
Tie = False

# This diplays the menu
Menu = True

# Shows us if space is pressed to avoid glitches
Space = False

# Lets the computer know when the player has played (just makes it faster then doing multiple "or" statements)
Player_Move = False

# Allows the player to play again without having to close and reoped pygame
Again = False

Computer_Decision = ""

# Setting text size and font
text_font = pygame.font.SysFont("Oswald", 30)
text_font_R = pygame.font.SysFont("Oswald", 100)

def Text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# When the game is running
run = True
while run:

    image = pygame.image.load('Rock Paper Scissors Background.png')
    screen.blit(image,(0, 0))

    if Menu == True:
        image = pygame.image.load('Menu.png')
        screen.blit(image,(0, 0))
    
    # If player presses 1, 2, or 3 it will results in Rock, Paper, or Scissors
    key = pygame.key.get_pressed()
    if key[pygame.K_1] == True and Computer_Decision  == "" and Player_Paper == False and Player_Scissors == False:
        Menu = False
        Player_Rock = True
        Player_Move = True
    elif key[pygame.K_2] == True and Computer_Decision  == "" and Player_Rock == False and Player_Scissors == False:
        Menu = False
        Player_Paper = True
        Player_Move = True
    if key[pygame.K_3] == True and Computer_Decision  == "" and Player_Rock == False and Player_Paper == False:
        Menu = False
        Player_Scissors = True
        Player_Move = True
    if key[pygame.K_SPACE] == True:
        Again = True

    # Randomizes computer choice
    if Player_Move == True:
        Computer_Decision  = random.randint(0, 2)
        Player_Move = False
        if Computer_Decision == 0:
            Computer_Rock = True
        if Computer_Decision  == 1:
            Compute_Paper = True
        if Computer_Decision  == 2:
            Computer_Scissors = True

    # This part determines who wins and gets a poin
    if Player_Rock == True:
        image = pygame.image.load('Rock.png')
        screen.blit(image,(0, 0))
        if Computer_Decision == 0:
            Tie = True
        if Computer_Decision == 1:
            Lose = True
        if Computer_Decision == 2:
            Win = True
    if Player_Paper == True:
        image = pygame.image.load('Paper.png')
        screen.blit(image,(0, 0))
        if Computer_Decision == 0:
            Win = True
        if Computer_Decision == 1:
            Tie = True
        if Computer_Decision == 2:
            Lose =  True
    if Player_Scissors == True:
        image = pygame.image.load('Scissors.png')
        screen.blit(image,(0, 0))
        if Computer_Decision == 0:
            Lose = True
        if Computer_Decision == 1:
            Win = True
        if Computer_Decision == 2:
            Tie = True

    if Computer_Decision == 0:
        image = pygame.image.load('Computer Rock.png')
        screen.blit(image,(0, 0))
    if Computer_Decision == 1:
        image = pygame.image.load('Computer Paper.png')
        screen.blit(image,(0, 0))
    if Computer_Decision == 2:
        image = pygame.image.load('Computer Scissors.png')
        screen.blit(image,(0, 0))
            
    # Displays if player wins, loses, or ties
    if Win == True:
            Text("Win", text_font_R, (0, 0, 0), 200, 400)
            Text("Press space to play again", text_font, (0, 0, 0), 150, 700)
    if Lose == True:
            Lose = False
            Text("Lose", text_font_R, (0, 0, 0), 200, 400)
            Text("Press space to play again", text_font, (0, 0, 0), 150, 700)
    if Tie == True:
            Text("Tie", text_font_R, (0, 0, 0), 200, 400)
            Text("Press space to play again", text_font, (0, 0, 0), 150, 700)
    
            

    # This restarts the game (except score)
    if Again == True:
        Player_Rock = False
        Player_Paper = False
        Player_Scissors = False
        Computer_Rock = False
        Compute_Paper = False
        Computer_Scissors = False
        Computer_Decision = ""
        Player_Move = False
        Computer_Decision_Display = ""
        Again = False
        Win = False
        Lose = False
        Tie = False

    if Player_Rock == False and Player_Paper == False and Player_Scissors == False:
        Menu = True
    else:
        Menu = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()