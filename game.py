import random
import pygame
import math
from time import sleep

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((480, 480))

# Background
background = pygame.image.load('floor.png')
coin = pygame.image.load('coin2.jpg')

black = (0, 0, 0)
white = (255, 255, 255)

mode = 0

font = pygame.font.Font('freesansbold.ttf', 11)
text1 = font.render('You have made it into the soviet factory. You are in the entrance room of the factory.', True, black, white)
text2 = font.render('There is a hallway leading into the main room of the factory. ', True, black, white)
text3 = font.render('You hold nothing but a silenced pistol.And of course, some general tools that ', True, black, white)
text4 = font.render('can help on a stealth mission like this where you have to lurk ', True, black, white)



num = 0

pygame.display.set_caption("Perspectives") #Game title
icon = pygame.image.load('hero.png') #Imgae icon
pygame.display.set_icon(icon)

playerImg = pygame.image.load('hero.png') #Load in the image of the player
playerX = 400 #Player starting coordinates
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

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

for i in range(num_of_enemies): #Load number of enemies in a for loop
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 480)) #Spawn enemy at random x coordinate
    enemyY.append(random.randint(50, 150)) #Spawn enemy at random y coordinate
    enemyX_change.append(1)
    enemyY_change.append(20)

wall = pygame.image.load('wall2.png') #Load image of wall behind which hero hides

def player(x, y): #define function to place hero in certain coordinates
    screen.blit(playerImg, (x, y)) #scree.blit places image on the screen


def enemy(x, y, i): #define function to place enemy in certain coordinates
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0)) #Fill the screen with black
    # Background Image
    screen.blit(background, (0, 0)) #add background layer
    screen.blit(wall, (360, 370)) #add wall

    for event in pygame.event.get(): #if user presses x then quit
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1 #Change the value of playerX_change
            if event.key == pygame.K_RIGHT:
                playerX_change = 1 #Change the value of playerX_change
            if event.key == pygame.K_UP:
                playerY_change = -1 #Change the value of playerY_change
            if event.key == pygame.K_DOWN:
                playerY_change = 1 #Change the value of playerY_change
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x cordinate of the player
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP: #If user leaves the key, then stop moving
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change #Add the value of playerX_change to players x coordinate
    playerY += playerY_change #Add the value of playerY_change to players y coordinate

    if playerX <= 0: #If player goes outside the boundary teleport them back in
        playerX = 0
    elif playerX >= 459:
        playerX = 459
    if playerY <= 0:
        playerY = 0
    elif playerY >= 459:
        playerY = 459

    # Enemy Movement
    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            enemyImg = []
            enemyX = []
            enemyY = []
            enemyX_change = []
            enemyY_change = []
            num_of_enemies = 6

            for i in range(num_of_enemies): #Load number of enemies in a for loop
                enemyImg.append(pygame.image.load('enemy.png'))
                enemyX.append(random.randint(0, 480)) #Spawn enemy at random x coordinate
                enemyY.append(random.randint(50, 150)) #Spawn enemy at random y coordinate
                enemyX_change.append(1)
                enemyY_change.append(20)

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            del enemyX[i]
            del enemyY[i]
            del enemyX_change[i]
            del enemyY_change[i]
            num_of_enemies += -1
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 459:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY) #place player in the desired position
    pygame.display.update() #update the screen
