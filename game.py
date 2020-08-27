import random
import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((480, 480))

# Background
background = pygame.image.load('floor.png')

# Sound
mixer.music.load("soviet_march.wav")
mixer.music.play(-1)

pygame.display.set_caption("Perspectives")
icon = pygame.image.load('hero.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('hero.png')
playerX = 400
playerY = 400
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

wall = pygame.image.load('wall2.png')

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    screen.blit(wall, (360, 370))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
               
    playerX += playerX_change
    playerY += playerY_change
   
    if playerX <= 0:
        playerX = 0
    elif playerX >= 449:
        playerX = 449
    if playerY <= 0:
        playerY = 0
    elif playerY >= 449:
        playerY = 449
       
    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        enemy(enemyX[i], enemyY[i], i)
     
    player(playerX, playerY)
    pygame.display.update()