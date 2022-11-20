import pygame
import random
import math

#Initialize the pygame to use all functions of pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#background
background=pygame.image.load('spaceshipIcon/bg.jpg')

#Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('spaceshipIcon/i64.png')
pygame.display.set_icon(icon)


#Enemy
enemyImg = pygame.image.load('spaceshipIcon/enemy.png')
enemy_x=random.randint(0,735)
enemy_y=random.randint(40,150)

enemy_x_change= 0.1
enemy_y_change= 30


#Bullet
bulletImg = pygame.image.load('spaceshipIcon/bullet.png')
bullet_x=0
bullet_y=480
bullet_x_change= 0
bullet_y_change= .8
bullet_state='ready' #ready state means you cant see bullet on screen
# bullet_state='fire' #Bullet is moving currently
score=0

#collision Function
def iscollision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance=math.sqrt(math.pow(enemy_x-bullet_x,2)+math.pow(enemy_y-bullet_y,2))
    if distance < 27: #by trial and error method
        return True
    else:
        return False

#player
playerImg = pygame.image.load('spaceshipIcon/i64.png')
player_x=370
player_y=480

player_x_change=0


def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y):
    screen.blit(enemyImg,(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletImg,((x+16),(y+10)))

#Game loop
running=True 
while running:
    #RGB
    screen.fill((0, 0, 0))
    #backgrounf image
    # screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  #quit when close button is clicked
            running=False
            
        #if key is pressed check wheather it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3 
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_x=player_x
                    fire_bullet(bullet_x,bullet_y)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            
    player_x += player_x_change
    
    if player_x < 0:
        player_x =0
    elif player_x >= 736:
        player_x = 736
        
    enemy_x += enemy_x_change
    
    if enemy_x <= 0:
        enemy_x_change = 0.1
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.1
        enemy_y += enemy_y_change
        
    #Bullet movement
    if bullet_y <= 0:
        bullet_y=480
        bullet_state='ready'
    if bullet_state == 'fire':
        fire_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change
        
    #collision
    collision=iscollision(enemy_x,enemy_y,bullet_x,bullet_y)
    if collision:
        bullet_y=480
        bullet_state='ready'
        score+=1
        print(score)
        enemy_x=random.randint(0,735)
        enemy_y=random.randint(40,150)

        
        
    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    pygame.display.update()
    