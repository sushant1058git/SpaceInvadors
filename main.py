import pygame

#Initialize the pygame to use all functions of pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('spaceshipIcon/i64.png')
pygame.display.set_icon(icon)


#Enemy
enemyImg = pygame.image.load('spaceshipIcon/enemy.png')
enemy_x=370
enemy_y=50


#player
playerImg = pygame.image.load('spaceshipIcon/i64.png')
player_x=370
player_y=480

player_x_change=0


def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#Game loop
running=True 
while running:
    #RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  #quit when close button is clicked
            running=False
            
        #if key is pressed check wheather it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            
    player_x += player_x_change
    
    if player_x < 0:
        player_x =0
    elif player_x >= 736:
        player_x = 736
    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    pygame.display.update()
    