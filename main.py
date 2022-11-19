import pygame

#Initialize the pygame to use all functions of pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('spaceshipIcon/i64.png')
pygame.display.set_icon(icon)





#player
playerImg = pygame.image.load('spaceshipIcon/i64.png')
player_x=370
player_y=480


def player():
    screen.blit(playerImg,(player_x,player_y))

#Game loop
running=True 
while running:
    #RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  #quit when close button is clicked
            running=False
            
            
    player()
    pygame.display.update()
    